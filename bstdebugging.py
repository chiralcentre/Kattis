from sys import stdin

INF = pow(10,18)
def solve(n,m,arr):
    # BST invariant: if current value is X, all items in left subtree must be < X, all items in right subtree must be > X
    L,H = -INF,INF
    for i in range(n):
        v = arr[i]
        if v <= L or v >= H:
            return "invalid"
        if m < v:
            H = v
        elif m > v:
            L = v
        else:
            return "valid" if i == n - 1 else "invalid"
    return "valid"
    
n,m = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
print(solve(n,m,arr))
