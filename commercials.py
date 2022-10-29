from sys import stdin,stdout

#Kadane's algorithm
N,P = map(int,stdin.readline().split())
breaks = list(map(lambda x: int(x) - P, stdin.readline().split()))
overallMax,localMax = 0,0
for elem in breaks:
    localMax += elem
    if overallMax < localMax:
        overallMax = localMax
    if localMax < 0:
        localMax = 0
stdout.write(f"{overallMax}")
