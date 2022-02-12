""" Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """

def main():
    word = input("Ingrese una palabar: ").strip()
    if word == word[::-1]:
        print(f"la palabra {word.upper()} es polimdromo {word[::-1].upper()}")
    else:
        print(f"la palabra {word.upper()} no es polimdromo {word[::-1].upper()}")


if __name__ == "__main__":
    main()