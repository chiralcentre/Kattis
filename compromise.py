from sys import stdin,stdout

# take bit that happens most often at each location
for _ in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    freq = [{0: 0, 1: 0} for i in range(m)]
    for i in range(n):
        s = stdin.readline().strip()
        for j in range(m):
            char = int(s[j])
            freq[j][char] = freq[j].get(char,0) + 1
    for d in freq:
        stdout.write("0") if d[0] > d[1] else stdout.write("1")
    stdout.write("\n")
