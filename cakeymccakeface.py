from sys import stdin,stdout

N,M = int(stdin.readline()),int(stdin.readline())
entries,exits = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
time_difference = {}
#O(N*M)
for a in entries:
    for b in exits:
        if b - a >= 0:
            time_difference[b-a] = 1 if b - a not in time_difference else time_difference[b-a] + 1
secret,highest_value = 0,0
for key,value in time_difference.items():
    if value > highest_value:
        secret = key
        highest_value = value
    if value == highest_value and key < secret:
        secret = key
stdout.write(f"{secret}")
