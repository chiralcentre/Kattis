from sys import stdin,stdout
from math import sqrt

operands = {'-','*','+'}
def solve(grid,R):
    if R == 1: #no need for postfix conversion since only three operators are required
        stack = grid[0].split(' ')
        second = []
        while stack:
            s = stack.pop()
            if s == '-':
                second.append(-second.pop())
            elif s == '*':
                second.append(int(stack.pop()) * second.pop())
            elif s == '+':
                second.append(int(stack.pop()))
            elif s != '':
                second.append(int(s))
        return sum(second)
    elif R == 2:
        stack,i = [],0
        while i < len(grid[1]):
            #sqrt found
            if grid[1][i] == '\\' and grid[1][i+1] == '/':
                i += 2; j = i
                while j < len(grid[1]) and grid[0][j] == '_':
                    j += 1
                stack.append(int(sqrt(solve([grid[1][i:j]],1))))
                i = j
            elif grid[1][i] in operands:
                stack.append(grid[1][i])
                i += 1
            elif grid[1][i] != ' ':
                num = ""
                while i < len(grid[1]) and grid[1][i] != ' ':
                    num += grid[1][i]
                    i += 1
                stack.append(num)
            else:
                i += 1
        return solve([" ".join(str(char) for char in stack)],1)
    else: #three rows
        centre,stack,i = grid[1],[],0
        while i < len(centre):
            #sqrt found
            if centre[i] == '\\' and centre[i+1] == '/':
                i += 2; j = i
                while j < len(centre) and grid[0][j] == '_':
                    j += 1
                stack.append(int(sqrt(solve([centre[i:j]],1))))
                i = j
            elif centre[i] in operands:
                stack.append(centre[i])
                i += 1
            elif 48 <= ord(centre[i]) <= 57: #check for numbers
                num = ""
                while i < len(centre) and centre[i] != ' ':
                    num += centre[i]
                    i += 1
                stack.append(num)
            elif centre[i] == '=':
                j = i
                while j < len(centre) and centre[j] == '=':
                    j += 1
                t,b = solve([grid[0][i:j]],1),solve([grid[2][i:j]],1)
                stack.append(t//b)
                i = j
            else:
                i += 1
        return solve([" ".join(str(char) for char in stack)],1)
                
                
        
    
R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip("\n") for _ in range(R)]
stdout.write(f"{solve(grid,R)}\n")
