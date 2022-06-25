from sys import stdin,stdout

n = int(stdin.readline())
truth_values = stdin.readline().split()
circuit = stdin.readline().split()

stack,operations = [],{'*','-','+'}
for i in range(len(circuit)):
    #replace alphabets with truth values
    if circuit[i] not in operations:
        circuit[i] = truth_values[ord(circuit[i])-65]
        
for char in circuit:
    if char == '*':
        first,second = stack.pop(),stack.pop()
        stack.append('T') if first == 'T' and second == 'T' else stack.append('F')
    elif char == '+':
        first,second = stack.pop(),stack.pop()
        stack.append('F') if first == 'F' and second == 'F' else stack.append('T')
    elif char == '-':
        first = stack.pop()
        stack.append('F') if first == 'T' else stack.append('T')
    else:
        stack.append(char) #truth values

stdout.write(f"{stack[0]}")
        
