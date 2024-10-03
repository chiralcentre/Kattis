from sys import stdin,stdout

L,H,K = map(int,stdin.readline().split())
laptop = [["_" for i in range(L)] for j in range(H)]
for i in range(K):
    l,h,a,b = map(int,stdin.readline().split())
    for j in range(b, min(b + h, H)):
        for k in range(a, min(a + l, L)):
            laptop[j][k] = chr(97 + i)
stdout.write("\n".join("".join(row) for row in laptop))
stdout.write("\n")
