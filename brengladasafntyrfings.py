from sys import setrecursionlimit

# recursion depth is at most 25000 for unbalanced tree
setrecursionlimit(30000)

# at each value, do the following
# check if smaller value exists ("<"). if so, go to smaller value
# if no smaller value exists, write down current number "p"
# check if larger value exists (">"). if so, go to larger value
# go back up to higher value if it exists ("^")
def interact(msg):
    print(msg)
    return int(input())

def inorder(op = None):
    if op != None:
        if interact(op) == 0:
            return
    inorder("<")
    if interact("p") == 0:
        return
    inorder(">")
    if interact("^") == 0:
        return
    
inorder()
print("!")
