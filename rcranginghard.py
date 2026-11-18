from sys import stdin

# code runs in O(N) time where N is number of tokens
def solve():
    tokens = stdin.read().split()
    # return (dx,dy) turned clockwise by r quarter turns
    # r = 0,1,2,3
    def rotate(r,dx,dy):
        if r == 0:
            return dx,dy
        elif r == 1:
            return dy,-dx
        elif r == 2:
            return -dx,-dy
        elif r == 3:
            return -dy,dx

    def compose(A,B):
        rA,xA,yA = A
        rB,xB,yB = B
        x,y = rotate(rA,xB,yB)
        rC = (rA + rB) % 4
        return rC,xA + x,yA + y

    def power(T, n):
        pw = [(0,0,0)]
        for _ in range(4):
            pw.append(compose(pw[-1], T)) # pw[k] == T^k, k = 0..4
        q,r = divmod(n,4)
        _,X,Y = pw[4] # T^4 is a pure translation
        return compose((0, q*X, q*Y), pw[r])
    
    # the two recursive functions return ((net_rotation,dx,dy),index of first token not consumed)
    def instruction(idx):
        if tokens[idx] == "FORWARD":
            num = int(tokens[idx + 1])
            return (0,0,num),idx + 2 # always north, relative to entry
        elif tokens[idx] == "LEFT":
            return (3,0,0),idx + 1
        elif tokens[idx] == "RIGHT":
            return (1,0,0),idx + 1
        elif tokens[idx] == "DO":
            return procedures.get(tokens[idx + 1]),idx + 2
        elif tokens[idx] == "REPEAT":
            num = int(tokens[idx + 1])
            body,j = sequence(idx + 2)
            return power(body,num),j + 1 # consume END token

    def sequence(idx):
        acc = (0,0,0)
        while idx < len(tokens) and tokens[idx] != "END":
            t,idx = instruction(idx)
            acc = compose(acc,t)
        return acc,idx
    idx = 0
    total = (0,0,0)
    # store the movements for each procedure
    procedures = {}
    while idx < len(tokens):
        if tokens[idx] == "TO":
            name = tokens[idx + 1]
            body,j = sequence(idx + 2)
            procedures[name] = body
            idx = j + 1 # consume END
        else:
            t,idx = instruction(idx)
            total = compose(total,t)
    return f"{total[1]} {total[2]}"

print(solve())
