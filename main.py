"""
Atlas Entry Point
"""

from atlas.core.runtime import Runtime


def main():
    runtime = Runtime()
    runtime.start()


if __name__ == "__main__":
    main()
