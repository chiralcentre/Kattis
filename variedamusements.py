M = pow(10,9) + 7

#A[i] represents number of sequences of i rides that do not end with tilt a whirl
#B[i] represents number of sequences of i rides that do not end with roller coaster
#C[i] represents number of sequences of i rides that do not end with drop towers
A,B,C = [-1 for i in range(51)],[-1 for i in range(51)],[-1 for i in range(51)]
A[0] = B[0] = C[0] = 1
def recurseA(i):
    if A[i] != -1:
        return A[i]
    A[i] = b * recurseB(i - 1) + c * recurseC(i - 1)
    A[i] %= M
    return A[i]

def recurseB(i):
    if B[i] != -1:
        return B[i]
    B[i] = a * recurseA(i - 1) + c * recurseC(i - 1)
    B[i] %= M
    return B[i]

def recurseC(i):
    if C[i] != -1:
        return C[i]
    C[i] = b * recurseB(i - 1) + a * recurseA(i - 1)
    C[i] %= M
    return C[i]

    
n,a,b,c = map(int,input().split())
print((a * recurseA(n - 1) + b * recurseB(n - 1) + c * recurseC(n - 1)) % M)
