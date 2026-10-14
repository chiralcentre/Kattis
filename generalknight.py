col_mappings = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
rev_col_mappings = ["a", "b", "c", "d", "e", "f", "g", "h"]

def decode_pos(pos):
    r,c = pos[1],pos[0]
    return (int(r) - 1, col_mappings[c])

def encode_pos(r,c):
    return rev_col_mappings[c] + str(r + 1)

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

a,b = map(int,input().split())
movements = set()
for c in (-1,1):
    for d in (-1,1):
        e,f = a * c,b * d
        movements.add((e,f))
        movements.add((f,e))
px,py = decode_pos(input().strip())
reachable = [encode_pos(x,y) for x,y in possiblepositions(px,py,8,8)]
print(len(reachable))
if reachable:
    print(" ".join(sorted(reachable)))
