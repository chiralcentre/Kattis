from sys import stdin,stdout

N = int(stdin.readline())
answers = [stdin.readline().strip() for _ in range(N)]
students = []
for i in range(int(stdin.readline())):
    S = int(stdin.readline())
    correct = sum(stdin.readline().strip() == answers[j] for j in range(N))
    students.append((S,correct))
sort_order = stdin.readline().strip()
if sort_order == "STUDENT_ID_ASC":
    students.sort()
elif sort_order == "STUDENT_ID_DESC":
    students.sort(key = lambda x: -x[0])
elif sort_order == "GRADE_ASC":
    students.sort(key = lambda x: (x[1],x[0]))
else:
    students.sort(key = lambda x: (-x[1],x[0]))
for student_id,score in students:
    stdout.write(f"{student_id} {score}\n")
