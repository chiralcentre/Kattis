from sys import stdin

k = int(stdin.readline())
X = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
print(sum(pow(k,x) for x in X))
