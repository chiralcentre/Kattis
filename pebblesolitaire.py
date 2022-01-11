def possibleboards(board):
    return [board[:i] + ['-' if char == 'o' else 'o' for char in board[i:i+3]] + board[i+3:] for i in range(len(board)-2) if board[i:i+3] == ['-','o','o'] or board[i:i+3] == ['o','o','-']]

def pebblesolitaire(board):
    moves = 0
    visited = [] #record positions visited before
    # right coordinate keeps track of number of marbles
    S = [(board,board.count('o'))] # all possible board states to try
    lowest = 9999 #arbitrarily large number
    while S:
        pebbles,counter = S.pop(0)
        pospn = possibleboards(pebbles)
        if not pospn and counter < lowest:
            lowest = counter
        for pn in pospn:
            if pn not in visited:
                visited.append(pn)
                S.append((pn,pn.count('o')))
    return lowest
    
for _ in range(int(input())):
    board = list(input().strip())
    print(pebblesolitaire(board))
   
