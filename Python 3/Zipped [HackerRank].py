Student_id, subjects = input().split()
marks = [map(float, (input().split())) for i in range(int(subjects))]
student_marks = list(zip(*marks))

for i in range(len(student_marks)):
    average = sum(student_marks[i]) / len(student_marks[i])
    print('%.1f' % average)
