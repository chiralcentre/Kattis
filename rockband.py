from sys import stdin

def solve():
    M,S = map(int,stdin.readline().split())
    rows = [list(map(int,stdin.readline().split())) for _ in range(M)]
    F = set()
    for j in range(S):
        for i in range(M):
            F.add(rows[i][j])
        if len(F) == j + 1:
            return F
        
if __name__ == "__main__":
    songs = solve()
    print(len(songs))
    print(" ".join(str(s) for s in sorted(songs)))
