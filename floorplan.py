#note that n = (m + k)(m - k)
#if n is odd, it is always possible -> m = (n+1)/2, k = (n-1)/2
#if n is even, at least one factor must be even
#if either factor is even, the other factor must be even as well
#Proof: Assume m + k is even
#if m is even and k is even, m - k is even as well
#if m is odd and k is odd, m - k is even as well
#if n is even, n must be divisible by 4 since both factors are even
#if n is divisible by 4, m = (n+4)/4 and k = (n-4)/4

n = int(input())
if n%2 == 1:
    print(f"{(n+1)//2} {(n-1)//2}")
elif n%4 == 0:
    print(f"{(n+4)//4} {(n-4)//4}")
else:
    print("impossible")
    
