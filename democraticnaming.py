from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
freq = [{} for _ in range(m)]
for _ in range(n):
    city = stdin.readline().strip()
    for i in range(m):
        freq[i][city[i]] = freq[i].get(city[i], 0) + 1
for d in freq:
    letter,f = None,-1
    for k,v in d.items():
        if v > f:
            letter,f = k,v
        elif v == f and k < letter:
            letter = k
    stdout.write(letter)
        
