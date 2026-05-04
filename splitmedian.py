def retrieve(i, arr, memo, label):
    if i < 0:
        return float("-inf")
    if i >= len(memo):
        return float("inf")
    if memo[i] is None:
        print(f"? {label} {i+1}", flush=True)
        memo[i] = int(input())
    return memo[i]


n, m = map(int, input().split())
A_label, B_label = "A", "B"
# ensure m <= n
if m > n:
    n, m = m, n
    A_label, B_label = "B", "A"

A = [None] * n
B = [None] * m
k = (n + m + 1) // 2
l = max(0, k - m)
r = min(n, k)
while l + 1 < r:
    mid = (l + r) // 2
    a_left = retrieve(mid - 1, A_label, A, A_label)
    b_right = retrieve(k - mid, B_label, B, B_label)
    if a_left <= b_right:
        l = mid
    else:
        r = mid
a_left = retrieve(l - 1, A_label, A, A_label)
b_left = retrieve(k - l - 1, B_label, B, B_label)
print(f"! {max(a_left, b_left)}", flush=True)
