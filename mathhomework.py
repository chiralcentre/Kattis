from sys import stdin,stdout

b,d,c,L = map(int,stdin.readline().split())
firstMax,secondMax,thirdMax = L//b,L//d,L//c
solvable = False
for i in range(firstMax+1):
    for j in range(secondMax+1):
        for k in range(thirdMax+1):
            if i*b + j*d + k*c == L:
                stdout.write(f"{i} {j} {k}\n")
                solvable = True
if not solvable:
    stdout.write("impossible\n")
