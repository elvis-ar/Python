from math import pi
import random

def ordenamiento_recursivo(lista, flag):
    i=0
    # flag en igual a len(lista) y va disminuyendo en cada llamada recursiva
    if flag == 0:
        return 0
    else: 
        # recorremos toda la lista una vez y llanmamos la recursividad otra vez
        while i < (len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
            i += 1

        ordenamiento_recursivo(lista, flag-1)


def main():
    # creando lista aleatoria
    lista = [random.randint(1,100) for i in range(10)]
    print("-"*20)
    print(lista)
    # llamando a la funcion de ordenamiento recursivo
    ordenamiento_recursivo(lista, len(lista))
    print("-"*20)
    print(lista)

if __name__ == "__main__":
    main()