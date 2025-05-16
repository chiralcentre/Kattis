from sys import stdin,stdout
from math import pi

EPSILON = pow(10,-9)

def check_possible(pie_area, F, r):
    total = 0
    for A in pie_area:
        total += A // (r * r * pi)
    return total >= F + 1

for _ in range(int(stdin.readline())):
    N,F = map(int,stdin.readline().split())
    pies = list(map(int,stdin.readline().split()))
    pie_area = list(map(lambda x: pi * x * x, pies))
    L,H = 0,max(pies)
    while abs(H - L) >= EPSILON:
        M = (L + H) / 2
        if check_possible(pie_area,F,M):
            L = M
        else:
            H = M
    stdout.write(f"{L * L * pi}\n")
