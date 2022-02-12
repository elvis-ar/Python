""" Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista. """

def main():
    courses = ["Matematica", "Lengua", "Fisica", "Programacion", "Algebra"]
    for i in range(len(courses)):
        print(f"Yo estudio {courses[i]}")


if __name__ == "__main__":
    main()