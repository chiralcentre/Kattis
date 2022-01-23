import sys
# sys.stdin.readline() is way faster than input()
while True:
    n,m = [int(i) for i in sys.stdin.readline().split()]
    set1 = set()
    if n == 0 and m == 0:
        break
    for i in range(n):
        set1.add(int(sys.stdin.readline().strip()))
    count = 0
    for j in range(m):
        if int(sys.stdin.readline().strip()) in set1:
            count += 1 
    print(count)
