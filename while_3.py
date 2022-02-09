""" Generar un programa que al ingresar una cantidad n de números naturales, 
muestre la suma, el promedio, el valor máximo y el mínimo. """

def main():
    sum = 0
    average = 0
    value_max = 0
    value_min = 0
    count_numbers = 0
    flag = 0

    while flag == 0:
        number = int(input("Ingrese un numero: "))
        flag = int(input("Desea seguir ingresando numero(Si: 0/ No: 1): "))
        sum += number

        if number > value_max:
            value_max = number

        if count_numbers == 0:
            value_min = number

        if number < value_min:
            value_min = number

        count_numbers += 1

    average = sum / count_numbers

    print(f"La suma de los numeros fue: {sum}")
    print(f"El promedio de los numeros es: {average: .2f}")
    print(f"El valor maximo fue: {value_max}")
    print(f"El valor minimo fue: {value_min}")




if __name__ == "__main__":
    main()