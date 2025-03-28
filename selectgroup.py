from sys import stdin,stdout

groups = {}
selections = {"union","intersection","difference"}

def process(statement,i):
    op = statement[i]
    if op not in selections:
        return groups[op],i + 1
    else:
        a,j = process(statement,i + 1)
        b,k = process(statement,j)
        if op == "union":
            return a.union(b),k
        elif op == "intersection":
            return a.intersection(b),k
        elif op == "difference":
            return a.difference(b),k
        
for line in stdin:
    line = line.strip().split()
    if line[0] == "group":
        groups[line[1]] = set(line[3:])
    else: #selection statement
        ans,_ = process(line,0)
        stdout.write(" ".join(name for name in sorted(ans)))
        stdout.write("\n")
        ans = set()
        
        
