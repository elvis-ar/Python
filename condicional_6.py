""" pedir a usuario ingresar 3 numeros y ordenarlos de mayor a menor """

def main():
    number_1 = int(input("Ingrese el primer numero: "))
    number_2 = int(input("Ingrese el segundo numero: "))
    number_3 = int(input("Ingrese el tercer numero: "))

    if number_1 > number_2 and number_1 > number_3:
        if number_2 > number_3:
            print(f" {number_1} {number_2} {number_3} ")
        else:
            print(f" {number_1} {number_3} {number_2} ")

    elif number_2 > number_1 and number_2 > number_3:
        if number_1 > number_3:
            print(f" {number_2} {number_1} {number_3} ")
        else:
            print(f" {number_2} {number_3} {number_1} ")
    
    else:
        if number_2 > number_1:
            print(f" {number_3} {number_2} {number_1} ")
        else:
            print(f" {number_3} {number_1} {number_2} ")




if __name__ == "__main__":
    main()