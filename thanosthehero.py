from sys import stdin,stdout

N = int(stdin.readline())
worlds = list(map(int,stdin.readline().split()))
counter,highest = 0,worlds[N-1]
for i in range(N - 2, -1, -1):
    highest -= 1
    if worlds[i] >= highest:
        counter += worlds[i] - highest
    else:
        highest = min(highest,worlds[i])
    if highest == 0 and i > 0:
        counter = 1
        break
stdout.write(f"{counter}")
