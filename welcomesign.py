from sys import stdin,stdout

r,c = map(int,stdin.readline().split())
u = 0
for i in range(r):
    w = stdin.readline().strip()
    rem = c - len(w)
    s = rem // 2
    h = rem - s
    u += (rem % 2 != 0)
    stdout.write("." * s if u % 2 else "." * h)
    stdout.write(w)
    stdout.write("." * h if u % 2 else "." * s)
    stdout.write("\n")
