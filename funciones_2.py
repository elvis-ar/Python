import random
""" Escribir una función que reciba una muestra de números en una lista 
y devuelva otra lista con sus cuadrados. """

def sacar_cuadrado(lista):
    list_of_squares = [lista[i]**2 for i in range(len(lista))]
    return list_of_squares


def main():
    lista = [random.randint(1,100) for i in range(1,10)]
    print(lista)
    list_of_squares = sacar_cuadrado(lista)
    print(list_of_squares)


if __name__ == "__main__":
    main()