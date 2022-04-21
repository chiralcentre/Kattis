#if K > (n-1)//2, walk all the way
#else, K steps taken to walk to a multiple of K from 0 and (n-1)%K + 1 steps to walk to n - 1 from highest multiple of K
def greedy(n,K):
    return n - 1 if K > (n - 1)/2 else (n-1)%K + K + 1
                                                
n,K = map(int,input().split())
print(greedy(n,K))
