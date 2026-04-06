from sys import setrecursionlimit

setrecursionlimit(1000000)

# recursive backtracking, runs in O(2^n * n) time
def generate_all(s):
    res = []
    def dfs(i, path):
        if i == len(s):
            res.append(path)
            return
        if s[i] == '*':
            dfs(i + 1, path + '(')
            dfs(i + 1, path + ')')
        else:
            dfs(i + 1, path + s[i])
    dfs(0, "")
    return res

def is_balanced(seq):
    left_brackets = 0
    for char in seq:
        if char == "(":
            left_brackets += 1
        else:
            if not left_brackets:
                return False
            left_brackets -= 1
    return left_brackets == 0

# ignore number
input()
result = generate_all(input().strip())
for res in result:
    if is_balanced(res):
        print("YES")
        break
else:
    print("NO")
