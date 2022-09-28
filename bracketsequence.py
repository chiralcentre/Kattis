from sys import stdin,stdout

n = int(stdin.readline())
tokens = stdin.readline().split()
stack = []; outer = True #outer keeps track of whether its currently outside
MODULO = 10**9 + 7
for t in tokens:
    if t == ")":
        temp = 0 if outer else 1
        if outer:
            while stack and stack[-1] != "(":
                temp += stack.pop()
                temp %= MODULO
        else:
            while stack and stack[-1] != "(":
                temp *= stack.pop()
                temp %= MODULO
        stack.pop() #remove left bracket
        stack.append(temp)
        outer = not outer
    else:
        if t == "(":
            outer = not outer
            stack.append(t)
        else:
            stack.append(int(t))
#sum up tokens in stack
stdout.write(f"{sum(stack)%MODULO}")
                
    
