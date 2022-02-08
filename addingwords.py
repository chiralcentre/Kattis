import sys

#variables store key-value pairs
#values store value-key pairs
variables,values = {},{}
for line in sys.stdin:
    command = line.split()
    if command[0] == 'def':
        if command[1] not in variables:
            variables[command[1]] = int(command[2])
            values[int(command[2])] = command[1]
        else: #overwrite
            old_value = variables[command[1]]
            variables[command[1]] = int(command[2])
            values.pop(old_value)
            values[int(command[2])] = command[1]
    elif command[0] == 'calc':
        #flag variable checks if there are variables in calculations that have not been defined before
        operands,operators,flag = [],[],False
        # start from back in a stack structure
        for i in range(len(command)-2,0,-1): #ignore starting calc command and end = sign
            if i%2:
                operand = command[i]
                if operand in variables:
                    operands.append(variables[operand])
                else:
                    flag = True
                    break
            else:
                operators.append(command[i])
        if flag:
            command.append("unknown")
        else:
            while len(operands) > 1:
                sign = operators.pop()
                a,b = operands.pop(),operands.pop()
                operands.append(a+b) if sign == '+' else operands.append(a-b)
            result = operands.pop()
            command.append(values[result]) if result in values else command.append("unknown")
        print(' '.join(command[1:]))
    else: #clear command
        variables.clear()
        values.clear()
    
    
