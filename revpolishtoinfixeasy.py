from sys import stdin

ops = {"+", "-", "*", "/"}
stack = []
tokens = stdin.readline().split()
for t in tokens:
    if t not in ops:
        stack.append(t)
    else:
        b,a = stack.pop(),stack.pop()
        stack.append(f"({a}{t}{b})")
print(stack[0])
