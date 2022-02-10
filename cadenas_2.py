""" Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, 
otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. """

def main():
    user_name = input("Ingrese su nombre: ")

    user_name = user_name.split()

    # usando list list comprehension
    user_name = [item.capitalize() for item in user_name]

    # usando for
    """ for i in range(len(user_name)):
        user_name[i] = user_name[i].capitalize() """
    
    # a la lista, la volvemos a hacer cadena.
    user_name = " ".join(user_name)
    
    print(user_name.upper())
    print(user_name.lower())
    print(user_name)


if __name__ == "__main__":
    main()