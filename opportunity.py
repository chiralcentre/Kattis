from sys import stdin

# for each phone j, C(j) = max(max(x_i - x_j, 0) + max(y_i - y_j, 0) + max(z_i - z_j, 0)) for some 1 <= i <= n
# given three numbers a,b,c, max(a,0) + max(b,0) + max(c,0) = maximum sum by picking any subset of {a,b,c}
n = int(stdin.readline())
phones = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
running_max = [0 for _ in range(8)]
subset_members = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),
                  (1,0,0),(1,0,1),(1,1,0),(1,1,1)]
for triple in phones:
    for i in range(1,8):
        T = 0
        for j in range(3):
            if subset_members[i][j]:
                T += triple[j]
        running_max[i] = max(running_max[i],T)
best,ans = float("inf"),None
for k in range(n):
    C = 0
    for i in range(1,8):
        t = 0
        for j in range(3):
            if subset_members[i][j]:
                t += phones[k][j]
        C = max(C,running_max[i] - t)
    if C < best:
        best,ans = C,k + 1
print(f"{best} {ans}")
