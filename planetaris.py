from sys import stdin,stdout

n,a = map(int,stdin.readline().split())
finni = sorted(map(int,stdin.readline().split()))
battles = 0
for i in range(n):
    if a > finni[i]:
        a -= finni[i] + 1
        battles += 1
    else:
        break
stdout.write(f"{battles}")
    
