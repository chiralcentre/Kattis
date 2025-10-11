from sys import stdin

n = int(stdin.readline())
landmarks = {}
for _ in range(n):
    name,x,y = stdin.readline().split()
    landmarks[name] = (int(x),int(y))
seq = stdin.readline().split()
total = 0
for i in range(1,len(seq)):
    sx,sy = landmarks[seq[i - 1]]
    cx,cy = landmarks[seq[i]]
    total += abs(sx - cx) + abs(sy - cy)
print(total)
