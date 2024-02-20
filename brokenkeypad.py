precomp = [pow(10,i) - pow(9,i) for i in range(14)]

# returns number of integers with digit 7 from 1 to n inclusive
def fast_solve(n):
    ans,n = 0,str(n)
    # find largest power of 10 < n, let it be x
    # number of numbers containing digit 7 from 0 to 10 ^ x - 1 = 10 ^ x - 9 ^ x
    # use precomputed numbers
    for i in range(len(n)):
        p = len(n) - i - 1
        c = int(n[i])
        if c > 7:
            ans += (c - 1) * precomp[p] + pow(10,p)
        elif c < 7:
            ans += c * precomp[p]
        else:
            ans += c * precomp[p] + 1
            if i + 1 < len(n):
                ans += int(n[i + 1:])
            return ans
    return ans
    
a,b = map(int,input().split())
# principle of inclusion exclusion
print(fast_solve(b) - fast_solve(a - 1))
