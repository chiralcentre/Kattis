from sys import stdin

stack = []
for i in range(int(stdin.readline())):
    op = stdin.readline().strip()
    if op != "Undo":
        stack.append(op)
    elif stack:
        stack.pop()
new_stack = []
for char in stack:
    if char != "Backspace":
        new_stack.append(char)
    elif new_stack:
        new_stack.pop()
new_stack.append(">")
print("".join(new_stack))
