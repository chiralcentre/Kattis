from math import log,ceil

n,k = map(int,input().split())
# minimum height = smallest m where (1 - k^m)/(1 - k) >= n + 1
# maximum height is always n + 1
min_h = max(1,ceil(log(k + n * (k - 1))/log(k))) if k > 1 else n + 1
# minimum width is always 1
# maximum width = n - floor(n / k)
# add 1 to maximum width if n is divisible by k
max_w = n - n // k + (n % k == 0) if k > 1 else 1
print(f"{min_h} {n + 1}")
print(f"1 {max_w}")
