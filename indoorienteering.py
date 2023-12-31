from sys import stdin,stdout
from itertools import permutations

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def get_bit(num, bit):
    temp = (1 << bit) & num
    return 0 if temp == 0 else 1

# meet in the middle approach
# take 0 as starting point and loop over all possible middle points
# partition remaining points into 1st and 2nd half
# compute distances travelled in each half
# reduce to two sum problem
# code runs in O(n * 2^n * (n / 2)!)
def solve(n,L,adjMat):
    if n < 4: # can use brute force for small n
        for perm in permutations([i for i in range(n)]):
            d = sum(adjMat[perm[k]][perm[k + 1]] for k in range(n - 1)) + adjMat[perm[-1]][perm[0]]
            if d == L:
                return "possible"
    else:
        h = (n - 2) >> 1
        # m is the midpoint
        for m in range(1,n):
            for mask in range(1 << n):
                # checj if mask contains start, midpoint and correct number of vertices
                if not (mask & 1 or mask & (1 << m) or count_set_bits(mask) != h):
                    lengths = set()
                    # i = 0 represents node is in mask, i = 1 represents node is not in mask
                    for i in range(2):
                        curr = []
                        for j in range(1,n):
                            # don't push in middle point
                            # second condition pushes j into the list if i is 0 and position j is set to 1 in mask, and if i is 1 and position j is set to 0 in mask
                            if j != m and (i == 0) == (get_bit(mask,j) > 0):
                                curr.append(j)
                        # check if permutation is empty
                        if curr:
                            for perm in permutations(curr):
                                d = adjMat[0][perm[0]] + sum(adjMat[perm[k]][perm[k + 1]] for k in range(len(curr) - 1)) + adjMat[perm[-1]][m]
                                if d <= L: #check if distance is within range
                                    if i == 0:
                                        lengths.add(d)
                                    elif L - d in lengths:
                                        return "possible"
    return "impossible"
                                
                        
    
n,L = map(int,stdin.readline().split())
adjMat = [list(map(int,stdin.readline().split())) for _ in range(n)]
stdout.write(f"{solve(n,L,adjMat)}\n")
