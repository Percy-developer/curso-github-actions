
import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} estas usando python!")


if __name__ == "__main__":
    main()
