from sys import stdin,stdout

def f(x,y):
    if (x,y) in memo:
        return memo[(x,y)]
    if x <= 0 or y <= 0:
        return d
    total = sum(f(x - ab[i],y - ab[i+1]) for i in range(0,len(ab),2)) + c
    memo[(x,y)] = total
    return total

memo = {}
for _ in range(int(stdin.readline())):
    firstLine = list(map(int,stdin.readline().split()))
    c,d = firstLine[-2],firstLine[-1]
    ab = firstLine[:-2]
    xy = list(map(int,stdin.readline().split()))
    for i in range(0,len(xy),2):
        stdout.write(f"{f(xy[i],xy[i+1])}\n")
    stdout.write("\n")
    memo = {}
