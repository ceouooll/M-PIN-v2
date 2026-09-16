from __future__ import annotations

import copy
import uuid
from typing import Any

from .errors import AuthorityError, FriendFolderError, SessionError, ValidationError
from .wallet import Wallet


class SynchronizationSession:
    """Bounded Friend synchronization session.

    Observable lifecycle:
      Connect -> Load -> Runtime -> Owner Save? -> Commit or No-Save -> Disconnect
    """

    def __init__(
        self,
        wallet: Wallet,
        friend_id: str,
        *,
        owner_authorized: bool,
        create_if_missing: bool = False,
        owner_approved_create: bool = False,
    ):
        if not owner_authorized:
            raise AuthorityError("Owner authority is required before synchronization")
        if not friend_id or not isinstance(friend_id, str):
            raise ValidationError("friend_id must be a non-empty string")

        self.wallet = wallet
        self.friend_id = friend_id
        self.session_id = str(uuid.uuid4())
        self.active = False
        self.loaded_revision: int | None = None
        self.runtime_state: dict[str, Any] | None = None

        if not wallet.friend_exists(friend_id):
            if not create_if_missing:
                raise FriendFolderError("Friend Folder does not exist")
            wallet.create_friend_folder(friend_id, owner_approved=owner_approved_create)

        wallet._claim_active_session(self.session_id, friend_id)
        self.active = True
        self.load()

    def _require_active(self) -> None:
        if not self.active:
            raise SessionError("Session is terminated")

    def load(self) -> dict[str, Any]:
        self._require_active()
        revision, state = self.wallet.load_current(self.friend_id)
        self.loaded_revision = revision
        self.runtime_state = state
        return copy.deepcopy(state)

    def set_runtime_state(self, new_state: dict[str, Any]) -> None:
        self._require_active()
        if not isinstance(new_state, dict):
            raise ValidationError("Runtime state must be a JSON object")
        self.runtime_state = copy.deepcopy(new_state)

    def owner_save(self, *, owner_intent: bool) -> int:
        self._require_active()
        if not owner_intent:
            raise AuthorityError("Save requires explicit Owner persistence intent")
        if self.runtime_state is None or self.loaded_revision is None:
            raise SessionError("No loaded Runtime State")

        new_revision = self.wallet.commit(
            self.friend_id,
            self.runtime_state,
            expected_revision=self.loaded_revision,
        )
        self.loaded_revision = new_revision
        return new_revision

    def disconnect(self) -> None:
        if not self.active:
            return
        # Disconnect is explicitly NOT Save. Unsaved Runtime State simply disappears
        # relative to M-PIN persistence when this object is discarded.
        self.active = False
        self.runtime_state = None
        self.wallet._release_active_session(self.session_id)

    def __enter__(self) -> "SynchronizationSession":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.disconnect()
