import random
""" Escriba un programa que le permita al usuario intentar hasta cuatro veces la respuesta a una cierta pregunta. 
Si el usuario no acierta a los cuatro intentos,se le deberá indicar la respuesta correcta. """

def main():
    random_number = random.randint(1,20)
    count = 0

    while count < 4:
        print(f"-----Intento {count + 1}-----")
        user_number = int(input("Averigue el valor del numero escondigo, esta entre (1/10): "))

        if user_number == random_number:
            print(f"Felicidades..!! el numero escondido era el {random_number}")
            break

        count +=1

    if count == 4:
        print("Ups.. vuelva a intentarlo.")


if __name__ == "__main__":
    main()