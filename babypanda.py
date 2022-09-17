def solve(n,m):
    counter = 0
    while m > 0:
        if m%2:
            m -= 1
            counter += 1
        else:
            m //= 2
    return counter

n,m = map(int,input().split())
print(solve(n,m))
