""" Dadas las 4 notas obtenidas por un alumno, 
calcule e informe por pantalla su promedio 
e informe con una leyenda si está aprobado o no. 
La condición de aprobación es obtener un promedio mayor o igual que 4 """

def main():
    note_1 = int(input("Ingrese la primer nota: "))
    note_2 = int(input("Ingrese la segunda nota: "))
    note_3 = int(input("Ingrese la tercera nota: "))
    note_4 = int(input("Ingrese la cuarta nota: "))

    average = (note_1 + note_2 + note_3 + note_4) // 4

    if average >= 4:
        print(f"Estas aprobado con {average}")
    else:
        print(f"Estas desaprobado con {average}")


if __name__ == "__main__":
    main()