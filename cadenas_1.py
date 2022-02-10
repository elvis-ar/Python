""" Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. """

def main():
    user_name = input("Ingrese su nombre: ")
    count = int(input("Introdusca un numero: "))

    for i in range(count):
        print(i+1,user_name)


if __name__ == "__main__":
    main()