movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

class PuzzleState:
    def __init__(self,board):
        self.board = board
        self.r = len(board)
        self.c = len(board[0])
        self.empty_pos = self.get_empty_pos()
        
    def get_empty_pos(self):
        for i in range(self.r):
            for j in range(self.c):
                if self.board[i][j] == "-":
                    return (i,j)
        raise Exception("not supposed to happen")
    
    def generate_new_states(self):
        a,b = self.empty_pos
        output = []
        for x,y in possiblepositions(a,b,self.r,self.c,self.board):
            new_board = [row[:] for row in self.board]
            new_board[a][b] = new_board[x][y]
            new_board[x][y] = "-"
            output.append(PuzzleState(new_board))
        return output

    def hash(self):
        return "".join("".join(row) for row in self.board)

def solve(start,final_state):
    final_hash = final_state.hash()
    visited,moves,frontier = {start.hash()},0,[start]
    while frontier:
        new_frontier = []
        for u in frontier:
            if u.hash() == final_hash:
                return moves
            for v in u.generate_new_states():
                h =  v.hash()
                if h not in visited:
                    visited.add(h)
                    new_frontier.append(v)
        moves += 1
        frontier = new_frontier
    raise Exception("not supposed to happen")


final_state = PuzzleState([["1","2"],["3","-"]])
start = PuzzleState([list(input().strip()) for _ in range(2)])
print(solve(start,final_state))
