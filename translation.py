from sys import stdin,stdout

N = int(stdin.readline())
words = stdin.readline().split()
d = {}
for i in range(int(stdin.readline())):
    a,b = stdin.readline().split()
    d[a] = b
stdout.write(" ".join(d[w] for w in words))
