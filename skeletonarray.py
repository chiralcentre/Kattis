from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
# Let x be the starting number
# B[i] = x - sum of A[j] from j = 0 to i - 1
# Let T = sum of B = (N + 1) * x - C, where C is a constant, and C = (sum of A[j] from j = 0 to i - 1) for all i from i = 0 to i = N - 1
# If it is possible for f(x) to be 0 ((C) % (N + 1) = 0), output that answer
# If not, try the two values of x_1,x_2,x_2 = x1_1 + 1
# Note that there is only one unique solution where |T| is minimum
C,prefix = A[0],[A[0]]
for i in range(1,N):
    prefix.append(prefix[-1] + A[i])
    C += prefix[-1]
X = C // (N + 1)
output = []
if X * (N + 1) == C:
    output.append(X)
else:
    T1 = (N + 1) * X - C
    T2 = (N + 1) * (X + 1) - C
    if abs(T1) < abs(T2):
        output.append(X)
    else:
        output.append(X + 1)
for i in range(N):
    output.append(output[-1] - A[i])
print(" ".join(str(num) for num in output))
