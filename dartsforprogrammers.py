from sys import stdin,stdout

# precompute
board = [20,1,18,4,13,
         6,10,15,2,17,
         3,19,7,16,8,
         11,14,9,12,5]
total = sum(board)
board_indices = {board[i]: i for i in range(len(board))}
board_scores = [[-1 for i in range(20)] for j in range(20)]
for i in range(20):
    for j in range(i,20):
        board_scores[i][j] = board_scores[j][i] = sum(board[k] for k in range(i,j+1))
        
# assume u1 <= u2
def find_score(u1,u2):
    x,y = sorted([u1,u2])
    T = board_scores[x][y]
    return total - T + board[u1] + board[u2] if u1 > u2 else T

for _ in range(int(stdin.readline())):
    w1,w2,w3 = map(int,stdin.readline().split())
    u1,u2,u3 = board_indices[w1],board_indices[w2],board_indices[w3]
    # u1 <= u2 <= u3
    u1,u2,u3 = sorted([u1,u2,u3])
    stdout.write(f"{max(find_score(u1,u2),find_score(u2,u3),find_score(u3,u1))}\n")
