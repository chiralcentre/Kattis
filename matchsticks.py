from sys import stdin,stdout

sol = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20, 28, 68, 88, 108, 188, 200, 208, 288, 688, 888]

def smallest(n):
    ans = []
    while n > 20:
        ans.append(8)
        n -= 7
    # hard code small cases
    if n <= 20:
        ans.append(sol[n])
    return "".join(str(ans[i]) for i in range(len(ans) - 1, -1, -1))

def largest(n):
    ans = []
    while n > 3:
        ans.append(1)
        n -= 2
    ans.append(7) if n == 3 else ans.append(1)
    return "".join(str(ans[i]) for i in range(len(ans) - 1, -1, -1))

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    stdout.write(f"{smallest(n)} {largest(n)}\n")
