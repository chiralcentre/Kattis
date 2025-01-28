from sys import stdin,stdout

N,M,K = map(int,stdin.readline().split())
gradients = set()
for i in range(K):
    x,y = map(int,stdin.readline().split())
    gradients.add(y - x)
print(len(gradients))
