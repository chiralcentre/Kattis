from sys import stdin,stdout

#convert problem into interval covering problem
def solve(f):
    #find all possible intervals for each word
    #find largest possible set of non overlapping intervals
    intervals = []
    for w in words:
        e = f.find(w)
        while e != -1:
            intervals.append((e,e + len(w) - 1))
            e += 1
            e = f.find(w,e)
    #sort by increasing order of ending index, and take interval that end first
    intervals.sort(key = lambda x: x[1])
    ans,end = 0,-1
    for s,e in intervals:
        if s > end:
            end = e
            ans += 1
    return ans
            
words = []
while True:
    w = stdin.readline().strip()
    if w == "#":
        break
    words.append(w)

message = []
while True:
    m = stdin.readline().strip()
    if m == "#":
        break
    if m[-1] == "|":
        message.append(m[:-1])
        f = "".join(s for s in message)
        stdout.write(f"{solve(f)}\n")
        message = []       
    else:
        message.append(m)
