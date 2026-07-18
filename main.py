from airi.core import Airi
from airi.ui import banner, thinking


def main():
    airi = Airi()

    banner(
        version=airi.version,
        stage=airi.stage
    )

    airi.birth()

    print("\n🌸 AIRI siap berbicara dengan Papah.\n")

    while True:
        try:
            conversation = airi.chat()

            print(f"\n🗣️ Papah : {conversation['user']}")

            thinking()

            print(f"\n🌸 AIRI : {conversation['assistant']}\n")

        except KeyboardInterrupt:
            print("\n🌸 Sampai jumpa lagi, Papah!")
            break


if __name__ == "__main__":
    main()