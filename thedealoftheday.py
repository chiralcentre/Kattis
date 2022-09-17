from sys import stdin,stdout
from itertools import combinations

cardNums = list(map(int,stdin.readline().split()))
K = int(stdin.readline())
nonEmptyNums = [i for i in range(10) if cardNums[i] > 0]
if len(nonEmptyNums) < K:
    stdout.write("0")
else:
    counter = 0
    for c in combinations(nonEmptyNums,K):
        temp = 1
        for i in c:
            temp *= cardNums[i]
        counter += temp
    stdout.write(str(counter))
