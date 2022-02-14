def main():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    left = 0
    right = (len(lista)-1)

    number = int(input("Ingrese el numero que desea buscar: "))

    while left <= right:
        medium = ((left + right) // 2)
        if lista[medium] == number:
            print(f"el numero {number} se encuentra en la posicion {medium}")
            break
        if lista[medium] > number:
            right = medium - 1
        else:
            left = medium + 1

if __name__ == "__main__":
    main()