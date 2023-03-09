from sys import stdin,stdout

n,q = map(int,stdin.readline().split())
names,mappings = [],{}
for i in range(n):
    string = stdin.readline().strip()
    names.append(string)
    mappings[string] = i
for _ in range(q):
    a,b = stdin.readline().split()
    u,v = mappings[a],mappings[b]
    stdout.write(f"{abs(u - v) - 1}\n")
