from sys import stdin,stdout

# let us enumerate nodes starting from 0 instead of 1
# ith child of node x = x * K + i + 1 (assuming i is 0-indexed)
# parent of node x = floor((x - 1) / K)
# algorithm runs in O(Q * log_K(N))
def distance(x,y,k):
    if k == 1:
        return abs(x - y)
    moves = 0
    # when x = y, lowest common ancestor has been found
    while x != y:
        # invariant: x >= y
        if x < y:
            x,y = y,x
        # go to parent of node
        x = (x - 1) // k
        moves += 1
    return moves

N,K,Q = map(int,stdin.readline().split())
for i in range(Q):
    x,y = map(lambda x: int(x) - 1,stdin.readline().split())
    stdout.write(f"{distance(x,y,K)}\n")
