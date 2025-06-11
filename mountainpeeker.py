from sys import stdin

n,h = int(stdin.readline().strip()),int(stdin.readline().strip())
neg,pos = [],[]
for _ in range(n):
    x,y = map(int,stdin.readline().split())
    if x < 0: neg.append((x,y))
    else: pos.append((x,y)) # assume x != 0
neg.sort(); pos.sort()
grad = []
for i in range(len(neg) - 1, -1, -1):
    x,y = neg[i]
    g = ((y - h) / (-x))
    if not grad or g > grad[-1]:
        grad.append(g)
seen = len(grad)
grad = []
for x,y in pos:
    g = ((y - h) / x)
    if not grad or g > grad[-1]:
        grad.append(g)
print(seen + len(grad)) 
