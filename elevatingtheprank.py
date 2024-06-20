from sys import stdin,stdout

A,B = map(int,stdin.readline().split())
if A > B:
    A,B = B,A
floors_between = set()
for i in range(int(stdin.readline())):
    a = int(stdin.readline())
    if A < a < B:
        floors_between.add(a)
print((B - A) * 4 + len(floors_between) * 10)
