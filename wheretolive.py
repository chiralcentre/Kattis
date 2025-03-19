from sys import stdin,stdout
from math import floor,ceil

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    coords = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
    x_sum,y_sum = 0,0
    for x,y in coords:
        x_sum += x
        y_sum += y
    x_aver,y_aver = x_sum / n,y_sum / n
    xbase,ybase = [floor(x_aver),ceil(x_aver)],[floor(y_aver),ceil(y_aver)]
    best,x_ans,y_ans = pow(10,30),-1,-1
    for x in xbase:
        for y in ybase:
            total = sum((a - x) ** 2 + (b - y) ** 2 for a,b in coords)
            if total < best:
                best,x_ans,y_ans = total,x,y
    stdout.write(f"{x_ans} {y_ans}\n")
                
