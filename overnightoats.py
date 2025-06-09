from sys import stdin
from collections import deque

def solve():
    N,X = int(stdin.readline()),int(stdin.readline())
    oats = deque([])
    for i in range(N):
        line = stdin.readline().strip()
        if line == "ADD":
            oats.append(i)
        elif line == "EAT":
            u = oats.popleft()
            if i - u > X:
                return "ono.."
    return "yay!"

if __name__ == "__main__":
    print(solve())
