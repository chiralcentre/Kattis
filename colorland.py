from sys import stdin,stdout

def solve(colours,N):
    moves,curr = 0,0
    while curr != N:
        best = -1
        for col in colours:
            lst = colours[col]
            while lst and lst[-1] <= curr:
                lst.pop()
            if lst:
                best = max(best,lst[-1])
        moves += 1; curr = best
    return moves

N = int(stdin.readline())
colours = {"Blue": [], "Orange": [], "Pink": [],
           "Green": [], "Red": [], "Yellow": []}
for i in range(N):
    colours[stdin.readline().strip()].append(i + 1)
for col in colours:
    colours[col].reverse()
stdout.write(str(solve(colours,N)))
