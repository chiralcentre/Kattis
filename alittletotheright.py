from sys import stdin

# code runs in O(pn log n)
n,p = map(int,stdin.readline().split())
trophies = []
for i in range(n):
    properties = list(map(int,stdin.readline().split()))
    properties.append(i)
    trophies.append(tuple(properties))
    
unique_arrangements = set()
for i in range(p):
    temp = sorted(trophies,key = lambda x: x[i])
    increasing = True
    for j in range(n - 1):
        if temp[j][i] == temp[j + 1][i]:
            increasing = False
            break
    if increasing:
        arrangement = tuple([item[-1] for item in temp])
        unique_arrangements.add(arrangement)
print(len(unique_arrangements))
