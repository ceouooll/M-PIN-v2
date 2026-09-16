from __future__ import annotations

import copy
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from .errors import FriendFolderError, ValidationError


class Wallet:
    """Minimal persistent M-PIN wallet used by the reference implementation.

    The wallet stores only the current authoritative state for each Friend Folder.
    It intentionally does not implement history, rollback, cloud sync, encryption,
    provider infrastructure, or recovery.
    """

    FORMAT = "mpin-reference-v0.1"

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._active_session_id: str | None = None
        self._active_friend_id: str | None = None
        if not self.path.exists():
            self._atomic_write({"format": self.FORMAT, "friend_folders": {}})

    def _read(self) -> dict[str, Any]:
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if data.get("format") != self.FORMAT:
            raise ValidationError("Unsupported wallet format")
        if not isinstance(data.get("friend_folders"), dict):
            raise ValidationError("Invalid friend_folders structure")
        return data

    def _atomic_write(self, data: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(
            prefix=self.path.name + ".",
            suffix=".tmp",
            dir=str(self.path.parent),
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_name, self.path)
        except Exception:
            try:
                os.unlink(tmp_name)
            except FileNotFoundError:
                pass
            raise

    def friend_exists(self, friend_id: str) -> bool:
        return friend_id in self._read()["friend_folders"]

    def create_friend_folder(self, friend_id: str, *, owner_approved: bool) -> None:
        if not owner_approved:
            raise FriendFolderError("First Friend Folder creation requires Owner approval")
        data = self._read()
        folders = data["friend_folders"]
        if friend_id in folders:
            return
        folders[friend_id] = {"revision": 0, "current_state": {}}
        self._atomic_write(data)

    def load_current(self, friend_id: str) -> tuple[int, dict[str, Any]]:
        data = self._read()
        try:
            folder = data["friend_folders"][friend_id]
        except KeyError as exc:
            raise FriendFolderError(f"No Friend Folder bound to {friend_id!r}") from exc
        return int(folder["revision"]), copy.deepcopy(folder["current_state"])

    def commit(self, friend_id: str, proposed_state: dict[str, Any], *, expected_revision: int) -> int:
        if not isinstance(proposed_state, dict):
            raise ValidationError("Reference payload must be a JSON object")

        data = self._read()
        try:
            folder = data["friend_folders"][friend_id]
        except KeyError as exc:
            raise FriendFolderError(f"No Friend Folder bound to {friend_id!r}") from exc

        current_revision = int(folder["revision"])
        if current_revision != expected_revision:
            raise ValidationError(
                f"Stale save: expected revision {expected_revision}, current revision is {current_revision}"
            )

        new_revision = current_revision + 1
        folder["revision"] = new_revision
        folder["current_state"] = copy.deepcopy(proposed_state)
        self._atomic_write(data)
        return new_revision

    def _claim_active_session(self, session_id: str, friend_id: str) -> None:
        if self._active_session_id is not None:
            raise ValidationError(
                f"One Active Friend invariant: session {self._active_session_id} is already active"
            )
        self._active_session_id = session_id
        self._active_friend_id = friend_id

    def _release_active_session(self, session_id: str) -> None:
        if self._active_session_id == session_id:
            self._active_session_id = None
            self._active_friend_id = None

    def snapshot(self) -> dict[str, Any]:
        """Diagnostic view for tests/demo. Not a cross-Friend Session API."""
        return copy.deepcopy(self._read())
