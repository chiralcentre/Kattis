from sys import stdin,stdout

memo = {"": 1}
def dp(s):
    global memo, words
    if s in memo:
        return memo[s]
    total = 0
    for w in words:
        if s.startswith(w):
            r = s[len(w):]
            total += dp(r)
    memo[s] = total
    return total
            
N = int(stdin.readline())
words = [stdin.readline().strip().lower() for _ in range(N)]
for _ in range(int(stdin.readline())):
    w = stdin.readline().strip()
    stdout.write(f"{dp(w)}\n")
