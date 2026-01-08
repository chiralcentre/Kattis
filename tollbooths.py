from sys import stdin

balance,start = 0,0
for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    A = int(line[1])
    if line[0] == "T":
        balance -= A
        start = max(start, -balance)
    else:
        balance += A
print(start)
