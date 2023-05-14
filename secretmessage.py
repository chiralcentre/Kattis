from sys import stdin,stdout
from math import sqrt,ceil

def rotate90Clockwise(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]

for _ in range(int(stdin.readline())):
    message = stdin.readline().strip()
    s = ceil(sqrt(len(message)))
    m = [["*" for i in range(s)] for j in range(s)]
    for i in range(len(message)):
        m[i // s][i % s] = message[i]
    m = rotate90Clockwise(m)
    for i in range(s):
        for j in range(s):
            if m[i][j] != "*":
                stdout.write(m[i][j])
    stdout.write("\n")
