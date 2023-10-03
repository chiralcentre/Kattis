from math import floor,log2

# relevant link: https://www.quora.com/How-can-one-find-the-odd-coefficients-in-bionominal-expansion-of-x-1-1000-or-even-higher-powers
def solve(N):
    if N == 0:
        return 1
    return 2 * solve(N - pow(2,floor(log2(N))))
    
N = int(input())
print(solve(N))
