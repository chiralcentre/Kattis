from sys import stdin

def solve():
    n = int(stdin.readline())
    arr = [0]
    arr.extend(list(map(int,stdin.readline().split())))
    arr.append(0)
    # first and last values are sentinel values
    # for i = 1 to i = n, check if a[i - 1] + a[i + 1] >= a[i]
    for i in range(1,n + 1):
        if arr[i - 1] + arr[i + 1] < arr[i]:
            return "impossible"
    return "possible"

print(solve())
