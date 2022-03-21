from sys import stdin,stdout

targets = {}
for i in range(int(stdin.readline())):
    target,*boundary = stdin.readline().split()
    if target not in targets:
        targets[target] = [tuple(map(int,boundary))]
    else:
        targets[target].append(tuple(map(int,boundary)))

for j in range(int(stdin.readline())): #O(mn)
    x,y = map(int,stdin.readline().split())
    counter = 0
    if "rectangle" in targets:
        for t in targets["rectangle"]:
            x1,y1,x2,y2 = t
            if x1 <= x <= x2 and y1 <= y <= y2:
                counter += 1
    if "circle" in targets:
        for t2 in targets["circle"]:
            x3,y3,r = t2
            if (x - x3)**2 + (y - y3)**2 <= r**2:
                counter += 1
    stdout.write(f"{counter}\n")
            
