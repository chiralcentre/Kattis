from sys import stdin,stdout

stack = []
for line in stdin:
    line = line.strip()
    if line == "quit":
        break
    if line == "+":
        stack.append(stack.pop() + stack.pop())
    elif line == "-":
        b,a = stack.pop(),stack.pop()
        stack.append(a - b)
    elif line == "/":
        b,a = stack.pop(),stack.pop()
        stack.append(a // b)
    elif line == "*":
        stack.append(stack.pop() * stack.pop())
    elif line == "^":
        b,a = stack.pop(),stack.pop()
        stack.append(pow(a, b))
    elif line == "dup":
        stack.append(stack[-1])
    elif line == "print":
        stdout.write(f"{stack[-1]}\n")
    elif line == "pop":
        stack.pop()
    elif line == "swap":
        stack[-1],stack[-2] = stack[-2],stack[-1]
    else: #integer
        stack.append(int(line))
