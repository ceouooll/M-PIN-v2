from pathlib import Path
import tempfile

from mpin_ref import SynchronizationSession, Wallet


ORBIT_A = {
    "project": {
        "name": "Orbit Task",
        "frontend": "React",
        "database": "SQLite",
        "next_milestone": "Prototype",
    }
}

ORBIT_B = {
    "project": {
        "name": "Orbit Task",
        "frontend": "Svelte",
        "backend": "Node.js",
        "database": "PostgreSQL",
        "api": "REST",
        "next_milestone": "Authentication",
    }
}


def main():
    with tempfile.TemporaryDirectory() as td:
        wallet_path = Path(td) / "OWNER.MPIN.json"
        wallet = Wallet(wallet_path)

        print("=== M-PIN Reference Implementation v0.1b Verified ===")

        # First relationship creation requires Owner approval.
        with SynchronizationSession(
            wallet,
            "ai.example",
            owner_authorized=True,
            create_if_missing=True,
            owner_approved_create=True,
        ) as session:
            print("CONNECT  : ai.example")
            print("LOAD     :", session.runtime_state)
            session.set_runtime_state(ORBIT_A)
            rev = session.owner_save(owner_intent=True)
            print(f"COMMIT   : revision {rev}")
        print("DISCONNECT")

        # Runtime change without Save must not persist.
        with SynchronizationSession(wallet, "ai.example", owner_authorized=True) as session:
            session.set_runtime_state(ORBIT_B)
            print("RUNTIME  : changed to Svelte/PostgreSQL")
            print("NO SAVE  : disconnecting")
        rev, current = wallet.load_current("ai.example")
        print(f"CURRENT  : revision {rev} -> {current}")

        # Reconnect, make the same runtime change, now Owner explicitly saves it.
        with SynchronizationSession(wallet, "ai.example", owner_authorized=True) as session:
            session.set_runtime_state(ORBIT_B)
            rev = session.owner_save(owner_intent=True)
            print(f"OWNER SAVE -> COMMIT: revision {rev}")
        rev, current = wallet.load_current("ai.example")
        print(f"CURRENT  : revision {rev} -> {current}")


if __name__ == "__main__":
    main()
