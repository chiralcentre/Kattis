from sys import stdin

n,m = map(int,stdin.readline().split())
working = {}
for _ in range(n):
    components = stdin.readline().strip().split(", ")
    for output in components:
        pc,code = output.split()
        if code == "0":
            working[pc] = working.get(pc,0) + 1
print(min(working.values())) if len(working) == m else print(0)
