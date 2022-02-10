""" Escribe un programa que permita calificar a un grupo de diez alumnos de la  escuela  secundaria.  
Por  teclado  se ingresan  el  nombre  y  las  tres  calificaciones  de  cada alumno y con esos datos el programa debe calcular e informar 
el promedio de cada alumno y decir si está aprobado o no; 
para aprobar se requiere un promedio de seis o más 
y haber obtenido al menos seis en la última de las tres calificaciones. 
Posteriormente el programa debe informar cuántos alumnos aprobaron y cuántos obtuvieron un promedio de al menos 8 puntos. """

import abc


def main():
    student_name = str
    average = 0
    notes = 0
    notes_sum = 0
    outstanding_students = 0
    flag = 1

    while flag != 0:
        student_name = input("Ingrese el nombre del alumno: ")
        average = 0
        notes_sum = 0
        for j in range(1,4):
            notes = int(input(f"Ingrese la nota {j}: "))
            # sumando las notas
            notes_sum += notes
        # sacando el promedio
        average = notes_sum / 3
        # validando que el promedio y la ultima nota sean mayor a 6
        if notes >= 6 and average >= 6:
            print(f"felicitaciones {student_name} estas Aprovado con un promedio de {average: 0.2f}")
            if average >= 8:
                outstanding_students += 1

        flag = int(input("0) SALIR // 1) continuar: \n"))

    print(f"ahi {outstanding_students} destacados con un promedio mayor o igual a 8")


if __name__ == "__main__":
    main()