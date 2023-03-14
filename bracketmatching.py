from sys import stdin,stdout

def solve(string):
    stack = []
    for char in string:
        if char in opening:
            stack.append(char)
        else:
            if not stack:
                return "Invalid"
            last = stack.pop()
            if opening[last] != char:
                return "Invalid"
    return "Invalid" if stack else "Valid"

n = int(stdin.readline())
opening = {"(": ")", "[": "]", "{": "}"}
string = stdin.readline().strip()
stdout.write(solve(string))
