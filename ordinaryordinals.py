#brackets(N) = 2**(N+1)
def brackets(N,M):
    return pow(2,N+1,M)

#for N >= 2, commas(N) = 2**(N-1) - 1   
def commas(N,M):
    if N <= 1:
        return 0
    return pow(2,N-1,M) - 1

N,M = map(int,input().split())
print((brackets(N,M) + commas(N,M))%M)
