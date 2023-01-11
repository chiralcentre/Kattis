from sys import stdin,stdout
from collections import deque

N,C = map(int,stdin.readline().split())
elems = list(map(int,stdin.readline().split()))
A = [0 for _ in range(N)]
#D array is needed to perform range update efficiently
#D[0] = A[0], D[i] = A{i] - A[i - 1]
#to update from index L to index R inclusive by X, D[L] += X and D[R+1] -= X
D = [0 for i in range(N+1)]
#perform sliding window algo as shown
s = e = 0;
#keep track of running total in each window
total,window = elems[0],deque([elems[0]])
#O(N)
while s <= N - 1:
    if s <= e: #update range
        D[s] += 1; D[e + 1] -= 1
    if e + 1 > N - 1:
        s += 1
    elif s <= e and total + elems[e + 1] > C:
        s += 1
        total -= window.popleft()
    else:
        e += 1
        total += elems[e]
        window.append(elems[e])

#print answer in O(N)
A[0] = D[0]
stdout.write(f"{A[0]}\n")
for i in range(1,N):
    A[i] = D[i] + A[i - 1]
    stdout.write(f"{A[i]}\n")
