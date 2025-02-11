from sys import stdin,stdout

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n >>= 1
        steps += 1
    return steps

# note that starting value < 10^6 with longest steps is 837799 with 524 steps
n = int(input())
best,ans = -1,-1
for i in range(1, n):
    steps = collatz_steps(i)
    if steps > best:
        best,ans = steps,i
print(ans)
