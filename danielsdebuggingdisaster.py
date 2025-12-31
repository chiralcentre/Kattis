from math import comb

K,N,R = float(input()),int(input()),int(input())
success = pow(1 - K, N)
fail = 1 - success
all_fail = pow(fail, R)
print(1 - all_fail)
