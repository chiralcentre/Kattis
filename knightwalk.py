class State:
    def __init__(self,r,c,prev):
        self.r = r
        self.c = c
        self.prev = prev

movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
col_mappings = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
rev_col_mappings = ["a", "b", "c", "d", "e", "f", "g", "h"]

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def decode_pos(pos):
    r,c = pos[1],pos[0]
    return (int(r) - 1, col_mappings[c])

def encode_pos(r,c):
    return rev_col_mappings[c] + str(r + 1)

def shortest_paths(sr, sc, er, ec):
    visited = [[False for _ in range(8)] for _ in range(8)]
    frontier, final = [State(sr, sc, None)], []
    visited[sr][sc] = True
    while frontier:
        new_frontier = []
        next_visited = []  # track what to mark after this layer
        for state in frontier:
            for x, y in possiblepositions(state.r, state.c, 8, 8):
                if not visited[x][y]:
                    s = State(x, y, state)
                    new_frontier.append(s)
                    next_visited.append((x, y))
                    if x == er and y == ec:
                        final.append(s)
        if final:
            break
        # mark all as visited after processing current layer to allow for visiting the same node twice via different paths
        for x, y in next_visited:
            visited[x][y] = True
        frontier = new_frontier
    ans = []
    for fs in final:
        path, curr = [], fs
        while curr:
            path.append(encode_pos(curr.r, curr.c))
            curr = curr.prev
        ans.append(" -> ".join(path[::-1]))
    return sorted(ans)

start,end = input().strip(),input().strip()
sr,sc = decode_pos(start)
er,ec = decode_pos(end)
print("\n".join(shortest_paths(sr,sc,er,ec)))
