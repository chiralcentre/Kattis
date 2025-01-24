from sys import stdin
from math import ceil

def check_win(n,S,A,life_points):
    exp = 0 
    for x in life_points:
        hp_left = x - n * A
        if hp_left > 0:
            exp += ceil(hp_left / S)
    return exp <= n
            
N,S,A = map(int,stdin.readline().split())
life_points = list(map(int,stdin.readline().split()))
L,H,ans = 0,N * pow(10,9),-1
while L <= H:
    M = L + ((H - L) >> 1)
    if check_win(M,S,A,life_points):
        H = M - 1
        ans = M
    else:
        L = M + 1
print(ans)
