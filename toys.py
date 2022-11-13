#general form of Josephus problem
#Let f(n,k) denote the position of the remaining toy when there are initially n toys with step length k
#Note f(n,k) = (f(n-1,k) + k) mod n with f(1,k) = 0

def f(n,k):
    ans = 0
    for i in range(1,n):
        ans = (ans + k) % (i+1)
    return ans

T,K = map(int,input().split())
print(f(T,K))
