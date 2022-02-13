import sys

variables = {}
for line in sys.stdin:
    statement = line.split()
    if len(statement) == 1: 
        try:
            n = int(statement[0])
            if n == 0: # line containing zero
                break
            else:
                print(n)
        except ValueError: #string
            print(variables[statement[0]]) if statement[0] in variables else print(statement[0])
    elif statement[1] == '=': # definition of variables
        variables[statement[0]] = int(statement[2])
    else: # arithmetic sum
        numbers, undefined = [],[]
        for i in range(len(statement)):
            if not i%2: # even indexed elements are the operands
                try: # the operand is a number
                    numbers.append(int(statement[i]))
                except ValueError: #the operand is a string
                    if statement[i] in variables:
                        numbers.append(variables[statement[i]])
                    else:
                        undefined.append(statement[i])
        if numbers:
            if undefined: # there are undefined variables
                if sum(numbers) > 0:
                    print(f'{sum(numbers)} + ',end='')
                print(' + '.join(undefined))
            else:
                print(sum(numbers))
        else:
            print(' + '.join(undefined))
            
            
