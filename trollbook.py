from sys import stdin,stdout

n = int(stdin.readline())
pages = ["" for _ in range(n)]
for _ in range(n):
    w,p = stdin.readline().split()
    pages[int(p) - 1] = w
stdout.write(" ".join(page for page in pages))
stdout.write("\n")
