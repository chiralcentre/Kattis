from sys import stdin,setrecursionlimit

setrecursionlimit(200000)
# avoid string concatenation to last step to avoid repeated string concatenation
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in order traversal
def emit(node, out):
    if node.left is None:
        out.append(node.val)
        return
    out.append("(")
    emit(node.left, out)
    out.append(node.val)
    emit(node.right, out)
    out.append(")")
    
ops = {"+", "-", "*", "/"}
stack = []
tokens = stdin.readline().split()
for t in tokens:
    if t not in ops:
        stack.append(Node(t))
    else:
        b,a = stack.pop(),stack.pop()
        stack.append(Node(t,a,b))
output = []
emit(stack[0], output)
print("".join(output))
