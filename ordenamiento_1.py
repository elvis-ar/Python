import random

def sort_list(lista):
    flag = 0
    while flag == 0:
        flag = 1
        # si el flag no detecta un cambio se sale del bucle.
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                flag = 0
    return lista


def main():
    lista = [random.randint(1,100) for i in range(1,10)]
    print(lista)
    ordered_list = sort_list(lista)
    print(ordered_list)


if __name__ =="__main__":
    main()