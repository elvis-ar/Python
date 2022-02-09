""" Desarrolla un algoritmo que le permita leer tres valores enteros e indique cuál es el mayo """

def main():
    number_1 = int(input("Ingrese el primer numero: "))
    number_2 = int(input("Ingrese el segundo numero: "))
    number_3 = int(input("Ingrese el tercer numero: "))

    if number_1 > number_2 and number_1 > number_3:
        print(f"el mayor es el numero: {number_1}")
    elif number_2 > number_1 and number_2 > number_3:
        print(f"el mayor es el numero: {number_2}")
    else:
        print(f"el mayor es el numero: {number_3}")


if __name__ == "__main__":
    main()