memo = {(0,0): 1}

def binom_coeff(i,j):
    if j > i or j < 0:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    res = binom_coeff(i - 1, j) + binom_coeff(i - 1, j - 1)
    memo[(i,j)] = res
    return res

N,K = map(int,input().split())
total = 0
for i in range(N + 1):
    for j in range(i + 1):
        result = binom_coeff(i,j)
        if result % K == 0:
            total += 1
print(total)

