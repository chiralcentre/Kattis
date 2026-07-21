from sys import stdin

h,n = map(int,stdin.readline().split())
mappings = {"standard": 0, "fire": 1, "ice": 2, "light": 3}
dmg = list(map(int,stdin.readline().split()))
T = sum(dmg[mappings[stdin.readline().strip()]] for _ in range(n))
print("dead") if T >= h else print(h - T)
