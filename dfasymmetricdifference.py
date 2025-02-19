from sys import stdin,stdout

# first DFA
n1,c1,s1,f1 = map(int,stdin.readline().split())
s1 -= 1
w = stdin.readline().strip()
fs1 = set(map(lambda x: int(x) - 1, stdin.readline().split()))
am1 = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n1)]

# second DFA
n2,c2,s2,f2 = map(int,stdin.readline().split())
s2 -= 1
stdin.readline().strip()
fs2 = set(map(lambda x: int(x) - 1, stdin.readline().split()))
am2 = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n2)]

# print DFA representing symmetric difference
fs3 = set()
for x in range(n1):
    for y in range(n2):
        # either x is a final state or y is a final state but not both
        if (x in fs1) ^ (y in fs2):
            fs3.add(x * n2 + y)
n3,s3,f3 = n1 * n2,s1 * n2 + s2,len(fs3)
stdout.write(f"{n3} {c1} {s3 + 1} {f3}\n")
stdout.write(f"{w}\n")
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
        
