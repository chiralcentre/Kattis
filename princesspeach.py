from sys import stdin,stdout

N,Y = map(int,stdin.readline().split())
found = {int(stdin.readline()) for _ in range(Y)}
for num in range(N):
    if num not in found:
        stdout.write(f'{num}\n')
stdout.write(f"Mario got {len(found)} of the dangerous obstacles.")
