from sys import stdin,stdout

N,C = map(int,stdin.readline().split())
fruits = list(map(int,stdin.readline().split()))
highest = 0
for i in range(N):
    temp,weight = 0,0
    for j in range(i,N):
        if weight + fruits[j] <= C:
            temp += 1
            weight += fruits[j]
    highest = max(temp,highest)
stdout.write(f"{highest}")
