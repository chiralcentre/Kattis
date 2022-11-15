from sys import stdin,stdout

def solve(N,P,total):
    if P == 100:
        return "impossible"
    #worst case is N == 30, P == 99, total = 30
    for i in range(1,3000):
        if 1 <= ((N + i)*P - total)/i <= 100:
            return str(i)
    return "impossible"
        
    
N,P = map(int,stdin.readline().split())
scores = list(map(int,stdin.readline().split()))
total = sum(scores)
stdout.write(solve(N,P,total))

    
