from sys import stdin,stdout

winners = {"X": "Johan", "O": "Abdullah"}
syms = ["X","O"]

def res(grid):
    # check rows
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] in winners:
            return winners[grid[i][0]]
    # check columns
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] in winners:
            return winners[grid[0][i]]
    # check diagonals
    if (grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]) and grid[1][1] in winners:
        return winners[grid[1][1]]
    return "ingen"

def end(grid):
    X,O = 0,0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                X += 1
            elif grid[i][j] == "O":
                O += 1
    return X == 5 and O == 4

grid = [stdin.readline().strip().split() for i in range(3)]
X,O = 0,0
for i in range(3):
    for j in range(3):
        if grid[i][j] == "X":
            X += 1
        elif grid[i][j] == "O":
            O += 1
            
# if X == O, Johan's turn elif X > O, Abdullah's turn
j_wins,a_wins,curr = False,False,int(X > O)
stack = [(tuple("".join(char for char in grid[i]) for i in range(3)),curr)]
while stack:
    state,c = stack.pop()
    temp = [list(row) for row in state]
    r = res(state)
    if r == "Johan":
        j_wins = True
        continue
    elif r == "Abdullah":
        a_wins = True
        continue
    elif end(state):
        continue
    for x in range(3):
        for y in range(3):
            if temp[x][y] == "_":
                temp[x][y] = syms[c]
                stack.append((tuple("".join(char for char in temp[i]) for i in range(3)),1 - c))
                temp[x][y] = "_"
    
if j_wins and not a_wins:
    stdout.write("Johan kan vinna\n")
elif not j_wins and a_wins:
    stdout.write("Abdullah kan vinna\n")
elif j_wins and a_wins:
    stdout.write("Abdullah och Johan kan vinna\n")
else:
    stdout.write("ingen kan vinna\n")

