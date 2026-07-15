from airi.core import Airi


def banner(version, stage):
    print("=" * 45)
    print("🌸            PROJECT AIRI            🌸")
    print("=" * 45)
    print(f"Version : v{version} - {stage}")
    print()


def main():

    airi = Airi()

    banner(
        version=airi.version,
        stage=airi.stage
    )

    airi.birth()


if __name__ == "__main__":
    main()