from sys import stdin,stdout

#median of subsequence = B -> subsequence must contain B
N,B = map(int,stdin.readline().split())
seq = list(map(int,stdin.readline().split()))
#unique index of B since every integer appears only once
index = seq.index(B)
#define a function diff(S) for subsequence S as difference in number of elements > B and number of elements < B
#B is median of S <-> S contains B and diff(S) = 0
#split S into two subsequence S_L and S_R,where S_L is left of B and S_R is right of B
#S has median B if diff(S_L) + diff(S_R) = 0
L,R = {},{}
lower,higher = 0,0
#calculate diff values for subsequences ending in B
for i in range(index,-1,-1):
    if seq[i] > B:
        higher += 1
    elif seq[i] < B:
        lower += 1
    diff = higher - lower
    L[diff] = 1 if diff not in L else L[diff] + 1
#calculate diff values for subsequences starting with B
lower,higher = 0,0
for i in range(index,N):
    if seq[i] > B:
        higher += 1
    elif seq[i] < B:
        lower += 1
    diff = higher - lower
    R[diff] = 1 if diff not in R else R[diff] + 1
total = sum(L[key] * R[-key] for key in L if -key in R)
stdout.write(f"{total}")

