from sys import stdin,stdout

# If every group has a positive value, then everyone can play loud.
# Otherwise, pick a group that only has a negative value. This musician forced to play quiet. Remove all positive occurrences of this musician from other groups.
# If any group with only positives becomes empty, it is impossible. Otherwise, continue with another group that only has a negative value.
# runs in O(L) time, where L is total number of literals
def solve(N,G,pos_lit,pos_count,neg_lit):
    # set every musician as loud at the start
    status = ["L" for _ in range(N + 1)]
    # check if there is any clause with only negative literals
    # note that at most one negative literal can be found per clause
    # essentially, check for clauses of length 1 with a negative literal
    queue = []
    for i in range(G):
        if pos_count[i] == 0:
            if neg_lit[i] == None:
                return "impossible",None
            queue.append(neg_lit[i])
    while queue:
        new_queue = []
        for x in queue:
            status[x] = "Q"
            for idx in pos_lit.get(x,[]):
                if pos_count[idx] == 0:
                    continue
                pos_count[idx] -= 1
                if pos_count[idx] == 0:
                    if neg_lit[idx] == None:
                        return "impossible",None
                    new_queue.append(neg_lit[idx])
        queue = new_queue
    return "possible",status

N,G = map(int,stdin.readline().split())
pos_lit,pos_count,neg_lit = {},[0 for _ in range(G)],[None for _ in range(G)]
for i in range(G):
    _,*lst = map(int,stdin.readline().split())
    for lit in lst:
        if lit > 0:
            if lit not in pos_lit:
                pos_lit[lit] = [i] 
            else:
                pos_lit[lit].append(i)
            pos_count[i] += 1
        else:
            neg_lit[i] = -lit
res,output = solve(N,G,pos_lit,pos_count,neg_lit)
stdout.write(res)
stdout.write("\n")
if res == "possible":
    for i in range(1,N + 1):
        stdout.write(output[i])
    stdout.write("\n")
