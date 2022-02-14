def main():
    lista = [10,20,30,40,50,60,70,80,90,100]
    number = int(input("Ingrese el numero que desea buscar: "))
    print(lista)
    for i in range(len(lista)):
        if number == lista[i]:
            print(f"el numero {number} esta en la posicion {i}")
            break


if __name__ == "__main__":
    main()