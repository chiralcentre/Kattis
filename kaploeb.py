from sys import stdin,stdout

l,k,s = map(int,stdin.readline().split())
timings,laps = {},{}
for _ in range(l):
    i,t = stdin.readline().split()
    i = int(i)
    m,sec = map(int,t.split("."))
    time = m * 60 + sec
    timings[i] = time if i not in timings else timings[i] + time
    laps[i] = 1 if i not in laps else laps[i] + 1

rankings = sorted(list(timings.items()), key = lambda x: (x[1],x[0]))
for i,t in rankings:
    if laps[i] == k:
        stdout.write(f"{i}\n")
