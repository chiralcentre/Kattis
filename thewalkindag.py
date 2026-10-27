from sys import stdin,stdout

N = int(stdin.readline())
adjList = []
for i in range(N):
    _,*neighbours = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList.append(neighbours)
# up[k][v] = node landed on after taking 2^k highest priority steps from v
# maximum k = 16, as 2^16 < 10^5 < 2^ 17
# no walk exceeds N - 1 steps since graph is a DAG
# up[k][v] = v if there is no valid path with 2^k highest priority steps from v
up = [[i for i in range(N)] for _ in range(17)]
# fill level 0
for i in range(N):
    if adjList[i]:
        up[0][i] = adjList[i][0] 
# fill level k using results of level k - 1
for L in range(1,17):
    for u in range(N):
        up[L][u] = up[L - 1][up[L - 1][u]]
# answer queries in O(Q + N log N) time
for _ in range(int(stdin.readline())):
    s,t = stdin.readline().split()
    s = int(s) - 1
    e,p = s,0
    while p < len(t):
        instr = t[p]
        num_str = []
        while p + 1 < len(t) and t[p + 1].isdigit():
            num_str.append(t[p + 1])
            p += 1
        num = int("".join(num_str)) if num_str else 1
        if instr == "~":
            bin_repr = bin(num)[2:]
            for i in range(len(bin_repr)):
                if bin_repr[i] == "1":
                    L = len(bin_repr) - i - 1
                    e = up[L][e]
        else:
            e = adjList[e][num - 1]
        p += 1
    stdout.write(f"{e + 1}\n")
