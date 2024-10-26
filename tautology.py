from sys import stdin,stdout
from itertools import product

def solve(assignments, line):
    for assign in assignments:
        stack = []
        for i in range(len(line) - 1, -1, -1):
            if line[i] in assign:
                stack.append(assign[line[i]])
            elif line[i] == "K":
                a,b = stack.pop(),stack.pop()
                stack.append(a and b)
            elif line[i] == "A":
                a,b = stack.pop(),stack.pop()
                stack.append(a or b)
            elif line[i] == "N":
                stack.append(not (stack.pop()))
            elif line[i] == "C":
                a,b = stack.pop(),stack.pop()
                stack.append(not (a == False and b == True))
            elif line[i] == "E":
                a,b = stack.pop(),stack.pop()
                stack.append(a == b)
        if stack[0] == False:
            return "not"
    return "tautology"

var = {"p", "q", "r", "s", "t"}
for line in stdin:
    line = line.strip()
    if line[0] == "0":
        break
    present = list({char for char in line if char in var})
    assignments = []
    for combi in product([True, False],repeat = len(present)):
        assignments.append({present[i]: combi[i] for i in range(len(combi))})
    stdout.write(solve(assignments, line))
    stdout.write("\n")
    
