""" funcion para probar pasaje por referencia en Python """

def sumar(num_1, num_2, sum):
    sum.append(num_1 + num_2)
    print("funcion sumar")
    print(sum[0])

def main():
    # en Python solo los tipos compuestos se pasan por referencia
    sum = []
    num_1 = 7
    num_2 = 5
    sumar(num_1, num_2, sum)
    print("funcion main")
    print(sum[0])


if __name__ == "__main__":
    main()