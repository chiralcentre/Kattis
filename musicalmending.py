# problem: convert an input sequence to a sequence x, x + 1, ..., x + n - 1 with minimal effort
# reduce to problem of minimising sum of absolute deviations
# perform sorting, take x to be the median
# minimum is achieved at median
from sys import stdin

def cost_to_convert(arr, x):
    return sum(abs(x + i - arr[i]) for i in range(len(arr)))

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
b = sorted([arr[i] - i for i in range(n)])
x = b[n // 2]
print(sum(abs(x - num) for num in b))
