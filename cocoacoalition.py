#one split is sufficient if a is divisible by n or m
#two splits suffice if a or n*m - a can be factored into a = x*y where x < n and y < m
#three splits are always enough
def solve(n,m,a):
    if not a%n or not a%m:
        return 1
    for i in range(1,n):
        if (not a%i and a//i < m) or (not (n*m-a)%i and (n*m-a)//i < m):
            return 2
    return 3
    
n,m,a = map(int,input().split())
print(solve(n,m,a))
