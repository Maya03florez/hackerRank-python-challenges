if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Calcular el promedio de las calificaciones para el estudiante dado
    if query_name in student_marks:
        average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print("{:.2f}".format(average_score))
    else:
        print("Student not found.")