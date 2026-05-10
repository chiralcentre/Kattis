from sys import stdin,stdout

freq = {}
n,k,m = map(int,stdin.readline().split())
seen = 0
while seen < n:
    line = stdin.readline().strip().split()
    for w in line:
        if len(w) >= m:
            freq[w] = freq.get(w,0) + 1
    seen += len(line)
res = sorted(freq.items(), key = lambda x: (-x[-1],x[0]))
for i in range(k):
    stdout.write(f"{res[i][0]} {res[i][1]}\n")
