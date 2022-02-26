from sys import stdin,stdout
#O(T) where T is number of test cases
for _ in range(int(stdin.readline())):
    blank_line = stdin.readline().strip()
    NCS,NE = map(int,stdin.readline().split())
    counter1,counter2,CS_students,Econs_students = 0,0,[],[]
    CS_total,Econs_total = 0,0
    #O(NCS + NE)
    while counter1+counter2 < NCS + NE:
        line = list(map(int,stdin.readline().split()))
        for student in line:
            if counter1 < NCS:
                CS_students.append(student)
                counter1 += 1
                CS_total += student
            else:
                Econs_students.append(student)
                counter2 += 1
                Econs_total += student
    CS_average,Econs_average = CS_total/NCS,Econs_total/NE
    # For a CS student to drop out of CS and go into Econs causing the average intelligence to increase,
    # the intelligence of the student must be < CS_average and > Econs_average
    # O(NCS)
    candidates = 0
    for person in CS_students:
        if person < CS_average and person > Econs_average:
            candidates += 1
    stdout.write(f'{candidates}\n')
        
