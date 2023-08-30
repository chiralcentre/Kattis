from sys import stdin,stdout

# Let ones(i) be number of ones up to position i in the sequence.
# Let p(i) be number of subsequences with 1 as the first digit and 2 for the remaining digits on the first i digits.
# If ith digit is 2 then p(i) = 2 · p(i − 1) + ones(i)
# Otherwise p(i) = p(i − 1)
# Answer is sum of p(i) over all positions i where there we have a 3.
# Time complexity O(n)

M = 1000000007
n = int(stdin.readline())
songs = list(map(int,stdin.readline().split()))
ones,p = [0 for _ in range(n)],[0 for _ in range(n)]
ones[0] += songs[0] == 1
for i in range(1,n):
    ones[i] += ones[i - 1] + (songs[i] == 1)
for i in range(1,n):
    p[i] = (p[i - 1] << 1) + ones[i] if songs[i] == 2 else p[i - 1]
    p[i] %= M
ans = 0
for i in range(n):
    if songs[i] == 3:
        ans += p[i]
        ans %= M
stdout.write(f"{ans}\n")
