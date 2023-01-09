from sys import stdin,stdout

#data structures used:
#stack of hashmaps mapping variables to their types 
#hashmaps mapping variables to stacks of their indices
stack,types,curr = [],{},{}
N = int(stdin.readline())
for _ in range(N):
    line = stdin.readline().strip().split(" ")
    if line[0] == "{":
        stack.append(curr)
        curr = {}
    elif line[0] == "}":
        prev = curr
        curr = stack.pop()
        for key in prev:
            if types[key][-1] == len(stack) + 1:
                types[key].pop()
    elif line[0] == "DECLARE":
        v,t = line[1],line[2]
        if v in curr:
            stdout.write("MULTIPLE DECLARATION\n")
            break
        curr[v] = t
        if v not in types:
            types[v] = [len(stack)]
        else:
            types[v].append(len(stack))
    else: #TYPEOF query
        v = line[1]
        if v not in types or not types[v]:
            stdout.write("UNDECLARED\n")
        else:
            lastIndex = types[v][-1]
            stdout.write(f"{curr[v]}\n") if lastIndex >= len(stack) else stdout.write(f"{stack[lastIndex][v]}\n")
            
            
        
