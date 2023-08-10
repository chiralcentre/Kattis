from sys import stdin,stdout

# O(N log N), where N is length of string
def solve(s):
    h = [0 for _ in range(len(s))]
    h[0] = ord(s[0]) - 97
    # compute prefix sum of hash value
    for i in range(1,len(s)):
        h[i] += h[i - 1] + ord(s[i]) - 97
    for i in range(1,len(s) // 2 + 1): # try all possible divisors
        if not len(s) % i:
            found,prev = True,h[i - 1]
            for j in range(2 * i - 1,len(s),i):
                if h[j] - h[j - i] != prev:
                    found = False
                    break
            if found:
                return s[:i]
    return "-1"

s = stdin.readline().strip()
stdout.write(solve(s))
