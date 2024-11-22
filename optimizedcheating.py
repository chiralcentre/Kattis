from sys import stdin,stdout
from collections import deque

class State:
    parent = None
    curr = None
    op = None
    
    def __init__(self,parent,curr,op):
        self.parent = parent
        self.curr = curr
        self.op = op

    def get_path(self):
        path = [self.op]
        c = self.parent
        while c.op != None:
            path.append(c.op)
            c = c.parent
        return path[::-1]

def calculate(op,a,b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a // b

# code runs in O(nm) time since there are a maximum of nm edges and n vertices
# BFS is run
def solve():
    n,m,k = map(int,stdin.readline().split())
    memory = [int(stdin.readline()) for _ in range(n)]
    seen = set()
    for i in range(n):
        if i != k - 1:
            seen.add(memory[i])
    if memory[k - 1] not in seen:
        return (0,[])
    ops = [(lambda x: (x[0], int(x[1])))(stdin.readline().split()) for i in range(m)]
    frontier = deque([State(None, memory[k - 1], None)])
    explored = {memory[k - 1]}
    while frontier:
        s = frontier.popleft()
        u = s.curr
        for j in range(len(ops)):
            p,v = ops[j]
            res = calculate(p,u,v)
            if res >= 0:
                new_state = State(s,res,j + 1)
                if res not in seen:
                    path = new_state.get_path()
                    return (len(path),path)
                elif res not in explored:
                    frontier.append(new_state)
                    explored.add(res)
    return (-1,[])
    

if __name__ == "__main__":
    ans,lst = solve()
    stdout.write(f"{ans}\n")
    if lst:
        for num in lst:
            stdout.write(f"{num}\n")
