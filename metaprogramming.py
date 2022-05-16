from sys import stdin,stdout

variables = {}
for line in stdin:
    command = line.split()
    if command[0] == "define": #define command
        num = int(command[1]); s = command[2]
        variables[s] = num
    else: #comparison command
        s1,sign,s2 = command[1],command[2],command[3]
        if s1 not in variables or s2 not in variables:
            stdout.write("undefined\n")
        else:
            v1,v2 = variables[s1],variables[s2]
            stdout.write("true\n") if (v1 < v2 and sign == "<") or (v1 == v2 and sign == "=") or (v1 > v2 and sign == ">") else stdout.write("false\n")
            
