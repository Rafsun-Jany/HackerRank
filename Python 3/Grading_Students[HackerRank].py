def gradingStudents(grades):
    new_grades = []
    for i in grades:
        if i < 38 or i%5 ==0:
            new_grades.append(i)
        else:
            k = i%5
            k = 5-k
            if k >= 3:
                new_grades.append(i)
            else:
                t = i + k
                new_grades.append(t)
    return new_grades


if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print(result)
