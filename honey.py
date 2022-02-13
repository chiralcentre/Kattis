#Let walks(x,y,s) be the number of walks on s steps starting from tbe coordinates x, y ending up in the origin x = y = 0.
# dictionary is used for memoisation
d = {(0,0,0):1}
def walks(x,y,s,d):
    if (x,y,s) in d:
        return d[(x,y,s)]
    if s == 0: # walks(x, y, 0) is 1 if x = y = 0, and 0 otherwise.
        d[(x,y,s)] = 0
        return 0
    # the cells in the hexagonal grid can be represented by x,y coordinates
    d[(x,y,s)] = (walks(x-1,y-1,s-1,d) + walks(x,y-1,s-1,d) + walks(x+1,y,s-1,d) + walks(x+1,y+1,s-1,d) + walks(x,y+1,s-1,d) + walks(x-1,y,s-1,d))
    return d[(x,y,s)]

for _ in range(int(input())):
    print(walks(0,0,int(input()),d))

