from sys import stdin

total = 0
for _ in range(int(stdin.readline())):
    t,d,p = stdin.readline().split()
    if d == "IN":
        total += int(p)
    else:
        total -= int(p)
print(total) if total > 0 else print("NO STRAGGLERS")
