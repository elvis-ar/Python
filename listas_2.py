import random
""" Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. """

def main():
    # la loteria tiene numeros del 1 al 49 y se extraen 8
    list = sorted([random.randint(1,49) for i in range(8)])
    print(list)

if __name__ == "__main__":
    main()