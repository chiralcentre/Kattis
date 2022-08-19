#problem can be transformed into only computing over interval [1,A]
#Let F(a) be function that computes S for interval [1,a]
#for interval [1,1], answer = 0
#for interval [1,2X], answer is X//2 + X - 2 + 2F(X)
#for interval [1,2X + 1], answer is F(2X) + f(2X+1)

MOD = 1000000007
memo = {}

def F(X):
    if X <= 1: return 0
    if X in memo: return memo[X]
    #split into odd and even parts
    #if X is even, odd part is even as well
    odd = (X+1)//2
    even = X//2
    result = (even + 2*odd - 2 + F(odd) + F(even))%MOD
    memo[X] = result
    return result

L,R = map(int,input().split())
print((F(R) - F(L - 1))%MOD)
