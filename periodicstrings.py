from math import sqrt

def right_rotate(w):
    return w[-1] + w[:-1]

def get_divisors(n):
    factors = {1,n}
    if not n%2:
        factors.add(2)
        factors.add(n // 2)
    for i in range(3,int(sqrt(n))+1): 
        if not n%i:
            factors.add(i)
            factors.add(n // i)
    return factors

# code runs in O(L^3 * d) where d is number of divisors
def solve():
    s = input().strip()
    L = len(s)
    divisors = sorted(get_divisors(L))
    for k in divisors:
        substrings = [s[:k]]
        for i in range(L // k - 1):
            substrings.append(right_rotate(substrings[-1]))
        possible = True
        for j in range(0, L, k):
            if s[j:j+k] != substrings[j // k]:
                possible = False
                break
        if possible:
            return k

if __name__ == "__main__":
    print(solve())
            
        
