""" Desarrolla un algoritmo que le permita leer un valor cualquiera N 
y escribir en la pantalla si dicho número es Positivo, Negativo o 0 (cero) """

def main():
    number = int(input("Ingrese un numero: "))
    if number > 0:
        print(f"El numero {number} es positivo")
    elif number == 0:
        print(f"El numero {number} es cero")
    else:
        print(f"El numero {number} es negativo")


if __name__ == "__main__":
    main()