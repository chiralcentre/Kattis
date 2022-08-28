from sys import stdin

def consistent():
    C,n = map(int,stdin.readline().split())
    capacity = 0
    for i in range(n):
        L,E,S = map(int,stdin.readline().split())
        if capacity < L:
            return "impossible"
        capacity -= L
        if capacity + E > C:
            return "impossible"
        capacity += E
        if (capacity != C and S > 0) or (i == n - 1 and S > 0):
            return "impossible"
    return "possible" if capacity == 0 else "impossible"

print(consistent())
    
