""" pedir al usuario ingresar dos numeros y 
mostrar los numeros primos entre esos intervalos. """

def main():
    number_one = int(input("Ingrese el primer numero: "))
    number_two = int(input("Ingrese el segundo numero: "))

    while number_one < number_two:
        iterator = 2
        flag = True
        while iterator < number_one:
            if number_one % iterator == 0 or number_one == 1:
                flag = False
                break
            iterator += 1
        if flag and number_one != 1:
            print(f"{number_one} SI es primo")
        """ else:
            print(f"{number_one} NO es primo") """

        number_one += 1


if __name__ == "__main__":
    main()