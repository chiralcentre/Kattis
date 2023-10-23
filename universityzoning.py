from sys import stdin,stdout

R,C,F,S,G = map(int,stdin.readline().split())
faculties = [[] for num in range(F)]
for i in range(F):
    k,*faculty_cells = map(int,stdin.readline().split())
    for j in range(0,k * 2,2):
        faculties[i].append((faculty_cells[j] - 1,faculty_cells[j + 1] - 1)) #zero indexing
students = [[] for num in range(F)]
for i in range(S):
    r,c,D,f = map(int,stdin.readline().split())
    students[f - 1].append((r - 1,c - 1,D)) #offset by 1 due to zero indexing
compliance = list(map(int,stdin.readline().split()))
movements,met = [],0
for i in range(F):
    faculties[i].sort() #sort cells in each faculty by ascending order of row, followed by column
    students[i].sort(key = lambda x: x[2]) # sort students by student number
    m,positioned = [],0
    for j in range(len(students[i])):
        r,c,D = students[i][j]
        x,y = faculties[i][j]
        diff = abs(r - x) + abs(c - y)
        if diff == 0:
            positioned += 1
        else:
            m.append(abs(r - x) + abs(c - y))
    temp = 0
    if compliance[i] > positioned:
        m.sort() #sort by ascending order of steps taken
        for k in range(compliance[i] - positioned):
            temp += m[k]
        movements.append(temp)
    else:
        met += 1
ans = 0
if met < G:
    movements.sort() # sort by ascending order of steps taken to meet compliance target for each faculty
    for i in range(G - met):
        ans += movements[i]
stdout.write(f"{ans}\n")
