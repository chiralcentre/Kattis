def solve(n,k):
    if n == 0: return "N"
    if n == 1: return "A"
    #in S_{n - 2}
    if k <= fib[n - 2]: return solve(n - 2, k)
    #in S_{n - 1}
    return solve(n - 1, k - fib[n - 2])

n,k = map(int,input().split())
UPPER_BOUND,fib = 10**18,[1,1]
while (c := fib[-2] + fib[-1]) < UPPER_BOUND:
    fib.append(c)
fib.append(fib[-2] + fib[-1]) #length of sequence is 88
n -= 1 #for zero indexing purposes
#position of subsequence kth letter is in repeats every 2 iterations
while n > len(fib): n -= 2
print(solve(n,k))
