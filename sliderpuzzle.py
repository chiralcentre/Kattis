from sys import stdin,stdout

def solve(puzzle,n):
    L = len(puzzle)
    visited = [False for _ in range(L)]
    frontier = [0]
    visited[0] = True
    while frontier:
        u = frontier.pop()
        m = puzzle[u]
        if m == 0:
            return f"Puzzle {n} is solvable."
        if u - m in range(L) and not visited[u - m]:
            frontier.append(u - m)
            visited[u - m] = True
        if u + m in range(L) and not visited[u + m]:
            frontier.append(u + m)
            visited[u + m] = True
    return f"Puzzle {n} is not solvable."
    
for i in range(int(stdin.readline())):
    puzzle = list(map(int,stdin.readline().split()))
    stdout.write(f"{solve(puzzle, i + 1)}\n")
