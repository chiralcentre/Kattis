from sys import stdin, stdout

def main():
    n, m = map(int, stdin.readline().split())
    adjList = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, stdin.readline().split())
        adjList[u].append(v)
        adjList[v].append(u)
    col = [2] * n  # Unassigned colors
    enem = [0] * n  # Enemy count per node
    for i in range(n):
        cnt = [0, 0, 0]
        for j in adjList[i]:
            cnt[col[j]] += 1
        color = 0 if cnt[0] <= 1 else 1
        cur = i
        while True:
            col[cur] = color
            ncur = -1
            for j in adjList[cur]:
                if col[j] == color:
                    enem[cur] += 1
                    enem[j] += 1
                    if enem[j] == 2:
                        ncur = j
                        for l in adjList[ncur]:
                            if col[l] == color:
                                enem[l] -= 1
                                enem[ncur] -= 1
            if ncur == -1:
                break
            cur = ncur
            color = 1 - color
    res = [[], []]
    for i in range(n):
        res[col[i]].append(i + 1)
    stdout.write(f"{1 + bool(res[1])}\n")
    for group in res:
        stdout.write(" ".join(map(str, group)) + "\n")

if __name__ == "__main__":
    main()
