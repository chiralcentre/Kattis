num = int(input())
counter = 0

while counter < num:
    inpt = list(map(int,input().split()))
    students,student_grades = inpt[0],inpt[1:]
    mean = sum(student_grades)/students
    AAstudents = 0
    for grade in student_grades:
        if grade > mean:
            AAstudents += 1
    print(f'{format((AAstudents/students)*100, ".3f")}%')
    counter += 1
