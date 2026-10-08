from sys import stdin

output,persons = [],[]
for _ in range(int(stdin.readline())):
    name,h = stdin.readline().split()
    persons.append((name,int(h)))
curr = persons[-1][1]
output.append(persons[-1][0])
for i in range(len(persons) - 2, -1, -1):
    if persons[i][1] > curr:
        curr = persons[i][1]
        output.append(persons[i][0])
print(" ".join(output[::-1]))
