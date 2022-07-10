from sys import stdin,stdout

n,s = map(int,stdin.readline().split())
refills,water = 0,s
for _ in range(n):
    order = stdin.readline().strip()
    usage = int(order[0]) + 1 if order[-1] == 'L' else int(order[0])
    if usage > water:
        water = s
        refills += 1
    water -= usage
stdout.write(f"{refills}")
        
