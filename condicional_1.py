""" Desarrolla un algoritmo que le permita leer un valor entero cualquiera N 
y escribir si dicho número es par o impar """

def main():
    number = int(input("Ingrese un numero: "))
    if number % 2 == 0:
        print(f"El numero {number}, es par")
    else:
        print(f"El numero {number}, es impar")


if __name__ == "__main__":
    main()