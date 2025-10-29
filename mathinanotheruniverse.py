# handle addition and subtraction first
line = input().split()
ops = {"+", "-","*","/"}
stack = []
for char in line:
    if char not in ops:
        if stack and stack[-1] == "+":
            stack.pop()
            stack[-1] += int(char)
        elif stack and stack[-1] == "-":
            stack.pop()
            stack[-1] -= int(char)
        else:
            stack.append(int(char))
    else:
        stack.append(char)
        
ans = stack[0]
i = 1
while i < len(stack):
    if stack[i] == "*":
        ans *= stack[i + 1]
    elif stack[i] == "/":
        ans /= stack[i + 1]
    else:
        raise Exception("not supposed to happen")
    i += 2
print(int(ans))
        
