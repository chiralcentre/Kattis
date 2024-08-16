from sys import stdin

def get_card_hash(suit, value):
    return suit * 14 + value

def solve(seen, p):
    best = pow(10,9) 
    #iterate through all suits and every triplet in O(1) time
    for i in range(1,5):
        for j in range(1,12):
            h1,h2,h3 = get_card_hash(i,j),get_card_hash(i,j+1),get_card_hash(i,j + 2)
            values = {seen[h1],seen[h2],seen[h3]}
            if -1 not in values:
                latest = max(values)
                best = min(best, max(latest - p,1))
            # minimum number of turns needed is 1
            if best == 1:
                return str(best)
    return "Neibb" if best == pow(10,9) else str(best)
    
# keep track of the earliest time each card has been seen
seen = [-1 for _ in range(70)]
n,p = map(int,stdin.readline().split())
for i in range(n):
    c,k = map(int,stdin.readline().split())
    h = get_card_hash(c,k)
    if seen[h] == -1:
        seen[h] = i + 1
print(solve(seen,p))
