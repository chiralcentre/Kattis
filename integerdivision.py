from sys import stdin,stdout

n,d = map(int,stdin.readline().split())
numbers = list(map(int,stdin.readline().split()))
quotients = {}
#O(n)
for num in numbers:
    q = num//d
    quotients[q] = 1 if q not in quotients else quotients[q] + 1
#O(n)
pairs = 0
for key in quotients:
    value = quotients[key]
    pairs += value*(value-1)//2
stdout.write(str(pairs))

