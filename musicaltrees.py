from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
taken = [False for _ in range(m)]; counter = 0
positions = sorted(list(map(int,stdin.readline().split()))) #O(n log n)
trees = sorted(list(map(int,stdin.readline().split()))) #O(m log m)
for i in range(n): #O(nm)
    lowest,index = 1000000000,-1 # use 1 billion to represent infinity
    for j in range(m):
        if abs(trees[j] - positions[i]) < lowest:
            lowest = abs(trees[j] - positions[i])
            index = j
        if trees[j] > positions[i] and trees[j] - positions[i] > lowest:
            break
    if not taken[index]:
        taken[index] = True
        counter += 1
stdout.write(f'{n-counter}')
