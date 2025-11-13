N,s = input().split()
N = int(N)
res = []
for i in range(N):
    shift = pow(2,i,26)
    res.append(chr(ord("A") + (ord(s[i]) - ord("A") + shift) % 26))
print("".join(res))
