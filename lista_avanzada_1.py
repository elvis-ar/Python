""" Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante. """

def main():
    # cree el abecedario con codigo ASCII
    alphabet = [chr(i) for i in range(97, 123)]
    print(alphabet)

    # puse el for para mostrar la lista con sus indices
    for i in range(len(alphabet)):
        if i%3 != 0 or i == 0:
            print(i, alphabet[i])

# modificamos la lista, le decimos que cuando la divicion de i%3 sea distinto a 0 o i valga 0 se guarde en la lista nueva
    modified_alphabet = [alphabet[i] for i in range(0, len(alphabet)) if i%3 != 0 or i == 0]
    print(modified_alphabet)

if __name__ == "__main__":
    main()