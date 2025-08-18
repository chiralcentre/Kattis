from sys import stdin,stdout

N = int(stdin.readline())
C,T = [],0
for i in range(N):
    c = int(stdin.readline())
    C.append(c)
    T += c
R = int(stdin.readline())
x = (R + T) // N + ((R + T) % N > 0)
for i in range(N):
    C[i] = x - C[i]
    if C[i] < 0:
        stdout.write("not possible")
        exit(0)
stdout.write("\n".join(str(num) for num in C))
