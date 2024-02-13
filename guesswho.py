from sys import stdin,stdout

# O(NQ)
N,M,Q = map(int,stdin.readline().split())
attributes = [stdin.readline().strip() for _ in range(N)]
pos = [i for i in range(N)]
for i in range(Q):
    A,c = stdin.readline().split()
    A = int(A) - 1
    new_pos = []
    for j in pos:
        if attributes[j][A] == c:
            new_pos.append(j)
    pos = new_pos
# at least one listed character has attributes consistent with queries
stdout.write(f"ambiguous\n{len(pos)}\n") if len(pos) > 1 else stdout.write(f"unique\n{pos[0] + 1}\n")
