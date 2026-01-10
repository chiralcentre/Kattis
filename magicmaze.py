from sys import stdin,stdout

actions = {"North": 0, "East": 1,
           "South": 2, "West": 3}
reverse_actions = ["North", "East","South", "West"]
mappings = [[0],[1],[2],[3]]

n = int(stdin.readline())
transformations = []
for _ in range(n):
    line = stdin.readline().split()
    if line[0] == "Move":
        act = actions[line[1]]
        stdout.write(f"{reverse_actions[mappings[act][-1]]}\n")
    elif line[0] == "Change":
        ori,new = actions[line[1]],actions[line[3]]
        transformations.append((ori,new))
        mappings[ori].append(new)
    else: # get rid of last m transformation actions
        m = int(line[4])
        for i in range(m):
            ori,_ = transformations.pop()
            mappings[ori].pop()
    
