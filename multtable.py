from math import sqrt

def factors(n,m):
    step = 2 if m%2 else 1 #if number is odd, it cannot be divided by multiples of 2
    answer = 0
    for i in range(1,min(int(sqrt(m))+1,n+1),step): #O(min(sqrt(m),n))
        if not m%i and m//i <= n:
            answer += 1
            if i != m//i:
                answer += 1
    return answer

N,M = map(int,input().split())
print((factors(N,M)))
