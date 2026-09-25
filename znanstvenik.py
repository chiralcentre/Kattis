from sys import stdin

# code runs in O(RC) time, rolling hash
def solve(R,C,grid):
    labels = [0 for _ in range(C)]
    for i in range(R - 1, -1, -1):
        row = grid[i]
        counter = {}
        for j in range(C):
            if (labels[j],row[j]) not in counter:
                counter[(labels[j],row[j])] = [j]
            else:
                counter[(labels[j],row[j])].append(j)
        step = 0
        for key,lst in counter.items():
            for idx in lst:
                labels[idx] = step
            step += 1
        if len(counter) == C:
            return i
    # no two columns of table are the same
    raise Exception("not supposed to happen")

R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(R)]
print(solve(R,C,grid))
