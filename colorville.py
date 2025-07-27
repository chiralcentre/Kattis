from sys import stdin,stdout
from bisect import bisect_right

# overall time complexity is O(T * c * log(s)) where T is number of test cases
def solve(n,s,c,board):
    colours = {}
    for i in range(s):
        if board[i] not in colours:
            colours[board[i]] = [i]
        else:
            colours[board[i]].append(i)
    players = {i: -1 for i in range(n)}
    cards = [stdin.readline().strip() for _ in range(c)]
    for i in range(c):
        p = i % n
        card = cards[i]
        colours_pos = colours.get(card[0],[])
        if not colours_pos:
            return f"Player {p + 1} won after {i + 1} cards."
        index = bisect_right(colours_pos, players[p])
        if index < len(colours_pos):
            players[p] = colours_pos[index]
            if colours_pos[index] == s - 1:
                return f"Player {p + 1} won after {i + 1} cards."
        else:
            return f"Player {p + 1} won after {i + 1} cards."
        if len(card) == 2:
            index = bisect_right(colours_pos, players[p])
            if index < len(colours_pos):
                players[p] = colours_pos[index]
                if colours_pos[index] == s - 1:
                    return f"Player {p + 1} won after {i + 1} cards."
            else:
                return f"Player {p + 1} won after {i + 1} cards."
    return f"No player won after {c} cards."
    
while True:
    n,s,c = map(int,stdin.readline().split())
    if n == 0:
        break
    board = stdin.readline().strip()
    stdout.write(f"{solve(n,s,c,board)}\n")
    
