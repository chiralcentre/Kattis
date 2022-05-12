from sys import stdin,stdout

def gameResult(N):
    used = set(); prev = stdin.readline().strip()
    used.add(prev)
    for i in range(N-1):
        curr = stdin.readline().strip()
        if curr[0] != prev[-1] or curr in used:
            return "Player 1 lost" if i%2 else "Player 2 lost"
        used.add(curr)
        prev = curr
    return "Fair Game"

stdout.write(gameResult(int(stdin.readline())))
