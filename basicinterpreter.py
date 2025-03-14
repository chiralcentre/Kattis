from sys import stdin,stdout

MOD = pow(2,32)
OFFSET = pow(2,31)

def add(a,b):
    return (a + b + OFFSET) % MOD - OFFSET

def sub(a,b):
    return (a - b + OFFSET) % MOD - OFFSET

def mul(a,b):
    return (a * b + OFFSET) % MOD - OFFSET

def div(a,b):
    return (int(a / b) + OFFSET) % MOD - OFFSET

def is_equal(a,b):
    return a == b

def is_gt(a,b):
    return a > b

def is_lt(a,b):
    return a < b

def is_ne(a,b):
    return a != b

def is_le(a,b):
    return a <= b

def is_ge(a,b):
    return a >= b
    
arithmetic_ops = {"+": add, "-": sub, "*": mul, "/": div}
conds = {"=": is_equal, ">": is_gt, "<": is_lt,
         "<>": is_ne, "<=": is_le, ">=": is_ge}

# initialise all uppercase variables as 0
variables,statements,statements_map = {chr(i): 0 for i in range(65,91)},[],{}
for line in stdin:
    line = line.strip().split(" ", 2)
    line[0] = int(line[0])
    if line[1] == "LET" or line[1] == "IF":
        line[2] = line[2].split(" ")
    statements.append(line)
    
# sort in ascending order of labels
statements.sort(key = lambda x: x[0])
for i in range(len(statements)):
    label = statements[i][0]
    statements_map[label] = i

s = 0
while s < len(statements):
    line = statements[s]
    if line[1] == "LET":
        t = line[2]
        u,x = t[0],t[2]
        if len(t) == 3:
            variables[u] = variables[x] if x.isupper() else int(x)
        else: # arithmetic statement
            y = t[4]
            a = variables[x] if x.isupper() else int(x)
            b = variables[y] if y.isupper() else int(y)
            variables[u] = arithmetic_ops[t[3]](a,b)
    elif line[1] == "IF":
        t = line[2]
        x,y = t[0],t[2]
        a = variables[x] if x.isupper() else int(x)
        b = variables[y] if y.isupper() else int(y)
        res = conds[t[1]](a,b)
        if res:
            s = statements_map[int(t[5])]
            continue
    else: # print or println
        value = line[2].replace('"',"") if line[2].startswith('"') else variables[line[2]]
        stdout.write(f"{value}")
        if line[1][-1] == "N":
            stdout.write("\n")
    s += 1
                

