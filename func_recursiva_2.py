import random

""" Escribir una funcion recursiva que encuentre el mayor elemento de una lista. """

def func_recursiva(index,lista,max):
    if index < len(lista):
        if lista[index] > max[0]:
            max[0] = lista[index]

        func_recursiva(index+1, lista, max)


def main():
    index = 0
    max = [0]
    lista = [random.randint(1,100) for i in range(10)]

    print(lista)
    
    # paso MAX como lista para que se modifique el valor en la otra funcion y me devuelva con el valor modificado.
    func_recursiva(index,lista,max)
    print(f"el valor maximo de la lista es: {max[0]}")


if __name__ == "__main__":
    main()