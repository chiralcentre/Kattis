from sys import stdin,stdout

#there are three possible solution candidates
#A,B or P_i + P_j // 2 for every pair (i,j)
#if any candidate X is even, replace with X - 1 and X + 1
N = int(stdin.readline())
boys = sorted(map(int,stdin.readline().split()))
A,B = map(int,stdin.readline().split())
distance,best = -1,-1
candidates = []
temp = min(abs(boys[i] - A) for i in range(N)) if A%2 else min(abs(boys[i] - A - 1) for i in range(N))
if temp > distance:
    distance = temp
    best = A if A%2 else A + 1
temp = min(abs(boys[i] - B) for i in range(N)) if B%2 else min(abs(boys[i] - B + 1) for i in range(N))
if temp > distance:
    distance = temp
    best = B if B%2 else B - 1
for i in range(N-1):
    midpoint = (boys[i] + boys[i+1]) // 2
    if midpoint%2:
        if A <= midpoint <= B:
            temp = min(midpoint - boys[i], boys[i+1] - midpoint)
            if temp > distance:
                distance = temp
                best = midpoint
    else:
        if A <= midpoint - 1 <= B:
            temp = min(midpoint - 1 - boys[i], boys[i+1] - midpoint + 1)
            if temp > distance:
                distance = temp
                best = midpoint - 1
        if A <= midpoint + 1 <= B:
            temp = min(midpoint + 1 - boys[i], boys[i+1] - midpoint - 1)
            if temp > distance:
                distance = temp
                best = midpoint + 1
stdout.write(f"{best}")
