from sys import stdin,stdout

# first DFA
n1,c1,s1,f1 = map(int,stdin.readline().split())
s1 -= 1
w = stdin.readline().strip()
fs1 = list(map(lambda x: int(x) - 1, stdin.readline().split()))
am1 = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n1)]

# second DFA
n2,c2,s2,f2 = map(int,stdin.readline().split())
s2 -= 1
stdin.readline().strip()
fs2 = list(map(lambda x: int(x) - 1, stdin.readline().split()))
am2 = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n2)]

# print DFA representing intersection
n3,s3,f3 = n1 * n2,s1 * n2 + s2,f1 * f2
stdout.write(f"{n3} {c1} {s3 + 1} {f3}\n")
stdout.write(f"{w}\n")
fs3 = [a * n2 + b for a in fs1 for b in fs2]
stdout.write(" ".join(str(num + 1) for num in fs3))
stdout.write("\n")
am3 = [[0 for _ in range(c1)] for i in range(n1 * n2)]
for i in range(n1):
    for j in range(n2):
        s = i * n2 + j
        for k in range(c1):
            am3[s][k] = am1[i][k] * n2 + am2[j][k]

for lst in am3:
    stdout.write(" ".join(str(num + 1) for num in lst))
    stdout.write("\n")
        
