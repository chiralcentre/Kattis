from sys import stdin

class Node:
    def __init__(self, val):
        self.x = val
        self.left = None
        self.right = None

    def num_null(self):
        if self.left is None and self.right is None:
            return 2
        if self.left is None or self.right is None:
            return 1
        return 0

    # Standard recursive insert function
    def insert(self, item):
        if item < self.x:
            if self.left is None:
                self.left = Node(item)
            else:
                self.left.insert(item)
        else:
            if self.right is None:
                self.right = Node(item)
            else:
                self.right.insert(item)

    # Returns True iff this and other have the same structure
    def same_structure(self, other):
        if self.num_null() == 2 and other.num_null() == 2:
            return True

        if self.num_null() != other.num_null():
            return False

        if self.num_null() == 1 and ((self.left is None and other.left is not None) or (self.right is None and other.right is not None)):
            return False

        result = True
        if self.left is not None:
            result = result and self.left.same_structure(other.left)
        if self.right is not None:
            result = result and self.right.same_structure(other.right)

        return result

# code runs in O(nk + n^2*k) time
n,k = map(int,stdin.readline().split())
trees = []
for i in range(n):
    prototypes = list(map(int,stdin.readline().split()))
    curr = Node(prototypes[0])
    for j in range(1,k):
        curr.insert(prototypes[j])
    trees.append(curr)
ans = 0
# do pairwise comparison
for i in range(n):
    unique = True
    for j in range(i + 1, n):
        if trees[i].same_structure(trees[j]):
            unique = False
            break
    if unique:
        ans += 1
print(ans)
    
    
