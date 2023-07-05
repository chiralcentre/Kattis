MAX_N,MOD = 3,pow(10,9) + 7
BASE = [[1,1,1],[1,0,0],[0,0,1]]

def mod(a,m):
    return ((a % m) + m) % m

def mat_mul(A,B):
    #assume matrix multiplication is possible
    ans = [[0 for i in range(MAX_N)] for j in range(MAX_N)]
    for i in range(MAX_N):
        for j in range(MAX_N):
            if A[i][j] == 0: continue
            for k in range(MAX_N): 
                ans[i][k] += mod(A[i][j], MOD) * mod(B[j][k], MOD);
                ans[i][k] = mod(ans[i][k], MOD);
    return ans

def eye(m):
    identity = [[0 for i in range(m)] for j in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1
    return identity

def mat_pow(mat, power):
    result = eye(MAX_N)
    if power == 0:
        return result
    while power > 0:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1
    return result

N = int(input())
res = mat_pow(BASE, N - 1)
print(mod((res[1][0] * 2 + res[1][1] + res[1][2]),MOD))
