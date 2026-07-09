"""
Atlas Enterprise Operating System (AEOS)
"""

SYSTEM_NAME = "Atlas Enterprise Operating System"
SYSTEM_VERSION = "0.1.0"
SYSTEM_STATUS = "Initializing"
CHAIRMAN = "Sreenivasa Kurma"


def boot():
    print("=" * 60)
    print(SYSTEM_NAME)
    print(f"Version   : {SYSTEM_VERSION}")
    print(f"Status    : {SYSTEM_STATUS}")
    print(f"Chairman  : {CHAIRMAN}")
    print("=" * 60)
    print("Atlas Core Online")
    print("=" * 60)


if __name__ == "__main__":
    boot()
