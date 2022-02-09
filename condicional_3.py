""" Desarrolla un algoritmo que le permita leer dos valores A y B 
e indicar si la suma de los dos números es par. """

def main():
    number_a = int(input("Ingrese un numero: "))
    number_b = int(input("Ingrese otro numero: "))
    numbers_sum = number_a + number_b

    if numbers_sum%2 == 0:
        print(f"La suma de los numeros {number_a} y {number_b} es par => {numbers_sum}")
    else:
        print(f"La suma de los numeros {number_a} y {number_b} es impar => {numbers_sum}")


if __name__ == "__main__":
    main()