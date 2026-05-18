from sys import stdin

# remove all spaces from string
M = pow(10,9) + 7
line = stdin.readline().strip().replace(" ","")
ops,vals,i,prefix = [],[],0,{"a","s","m"}
while i < len(line):
    if line[i] in prefix:
        ops.append(line[i])
        i += 4
    elif line[i] == ")":
        op = ops.pop()
        v = vals.pop()
        if op == "a":
            vals.append((v + vals.pop()) % M)
        elif op == "s":
            vals.append((v * v) % M)
        else:
            vals.append(min(v,vals.pop(),vals.pop()) % M)
        i += 1
    elif line[i].isnumeric(): # number
        num = []
        while i < len(line) and line[i].isnumeric():
            num.append(line[i])
            i += 1
        vals.append(int("".join(num)))
    else: # comma or opening bracket
        i += 1
print(vals[-1])
