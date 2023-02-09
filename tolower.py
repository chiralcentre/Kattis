from sys import stdin,stdout

def checkUpper(string):
    for i in range(len(string)):
        if i > 0 and string[i].isupper():
            return True
    return False

P,T = map(int,stdin.readline().split())
solved = 0
for i in range(P):
    temp = 0
    for j in range(T):
        if not checkUpper(stdin.readline().strip()):
            temp += 1
    if temp == T:
        solved += 1
stdout.write(f"{solved}\n")
