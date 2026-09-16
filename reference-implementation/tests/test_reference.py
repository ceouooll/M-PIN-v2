import json
import tempfile
import unittest
from pathlib import Path

from mpin_ref import (
    AuthorityError,
    FriendFolderError,
    SynchronizationSession,
    ValidationError,
    Wallet,
)


class ReferenceImplementationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "owner.mpin.json"
        self.wallet = Wallet(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def create_friend(self, friend_id="friend-a"):
        s = SynchronizationSession(
            self.wallet,
            friend_id,
            owner_authorized=True,
            create_if_missing=True,
            owner_approved_create=True,
        )
        s.disconnect()

    def test_owner_authority_required(self):
        with self.assertRaises(AuthorityError):
            SynchronizationSession(
                self.wallet,
                "friend-a",
                owner_authorized=False,
                create_if_missing=True,
                owner_approved_create=True,
            )

    def test_first_folder_creation_requires_owner_approval(self):
        with self.assertRaises(FriendFolderError):
            SynchronizationSession(
                self.wallet,
                "friend-a",
                owner_authorized=True,
                create_if_missing=True,
                owner_approved_create=False,
            )

    def test_disconnect_is_not_save(self):
        self.create_friend()
        s = SynchronizationSession(self.wallet, "friend-a", owner_authorized=True)
        s.set_runtime_state({"value": "temporary"})
        s.disconnect()
        rev, state = self.wallet.load_current("friend-a")
        self.assertEqual(rev, 0)
        self.assertEqual(state, {})

    def test_owner_save_commits_current_state(self):
        self.create_friend()
        s = SynchronizationSession(self.wallet, "friend-a", owner_authorized=True)
        s.set_runtime_state({"value": "persisted"})
        rev = s.owner_save(owner_intent=True)
        s.disconnect()
        self.assertEqual(rev, 1)
        current_rev, state = self.wallet.load_current("friend-a")
        self.assertEqual(current_rev, 1)
        self.assertEqual(state, {"value": "persisted"})

    def test_save_requires_owner_intent(self):
        self.create_friend()
        s = SynchronizationSession(self.wallet, "friend-a", owner_authorized=True)
        s.set_runtime_state({"value": 1})
        with self.assertRaises(AuthorityError):
            s.owner_save(owner_intent=False)
        s.disconnect()

    def test_one_active_friend(self):
        self.create_friend("friend-a")
        self.create_friend("friend-b")
        s1 = SynchronizationSession(self.wallet, "friend-a", owner_authorized=True)
        with self.assertRaises(ValidationError):
            SynchronizationSession(self.wallet, "friend-b", owner_authorized=True)
        s1.disconnect()

    def test_friend_folder_isolation(self):
        self.create_friend("friend-a")
        self.create_friend("friend-b")
        with SynchronizationSession(self.wallet, "friend-a", owner_authorized=True) as s:
            s.set_runtime_state({"secret": "A"})
            s.owner_save(owner_intent=True)
        rev_b, state_b = self.wallet.load_current("friend-b")
        self.assertEqual(rev_b, 0)
        self.assertEqual(state_b, {})

    def test_current_state_only_no_history(self):
        self.create_friend()
        with SynchronizationSession(self.wallet, "friend-a", owner_authorized=True) as s:
            s.set_runtime_state({"n": 1})
            s.owner_save(owner_intent=True)
            s.set_runtime_state({"n": 2})
            s.owner_save(owner_intent=True)
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        folder = raw["friend_folders"]["friend-a"]
        self.assertEqual(folder["revision"], 2)
        self.assertEqual(folder["current_state"], {"n": 2})
        self.assertNotIn("history", folder)

    def test_stale_write_rejected(self):
        self.create_friend()
        with SynchronizationSession(self.wallet, "friend-a", owner_authorized=True) as s:
            s.set_runtime_state({"n": 1})
            s.owner_save(owner_intent=True)
        with self.assertRaises(ValidationError):
            self.wallet.commit("friend-a", {"n": 999}, expected_revision=0)
        rev, state = self.wallet.load_current("friend-a")
        self.assertEqual(rev, 1)
        self.assertEqual(state, {"n": 1})


if __name__ == "__main__":
    unittest.main()
