from sys import stdin,stdout

def two_power(n):
    ans = 0
    while not n%2:
        n >>= 1
        ans += 1
    return ans

#runs in O(N log N) in worst case since there is at most log N duplicates of 2  
N,K = map(int,stdin.readline().split())
exponent = sum(two_power(int(stdin.readline())) for i in range(N))
stdout.write("1") if exponent >= K else stdout.write("0")
