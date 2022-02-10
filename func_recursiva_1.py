""" Escriba una función recursiva que implemente:
a)Mostrar los números del 1 al N en orden creciente.
b)Mostrar los números del 1 al N en orden decreciente. """

def recursiva(initial,num):
    print(initial)
    if initial < num:
        recursiva(initial+1, num)
    if initial == num:
        print("-" * 20)
    print(initial)


def main():
    number = int(input("Ingrese hasta que numero quiere ver la recursividad: "))
    initial =1
    recursiva(initial,number)


if __name__ == "__main__":
    main()