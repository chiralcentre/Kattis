from sys import stdin

M = pow(10,9) + 7
# modular inverse of 2
# by Fermat's little theorem, since M is prime, for any integer a not divisible by M, a^{M - 1} = 1 (mod M)
# a^{M - 2) = a^{-1} (mod M)
# a^{M - 2} mod M is the modular inverse of a
inv2 = pow(2, M - 2, M)   
# number of inversions of a 0-1 sequence = number of pairs (i,j) with i < j, s_i = 1, s_j = 0
# how many of the 2^k fillings satisfy s_i = 1, s_j = 0 depends only on original characters at i and j
# if both are not ?: contributes 2^k if s_i = 1, s_j = 0, else 0
# if one is fixed, the other is 0 (fixed 1 before ? or fixed ? before 0): contributes 2^{k - 1}
# both ?: both get pinned, k - 2 remains free, contributes 2^{k - 2}
seq = stdin.readline().strip()
A,B,k = 0,0,0
# ones = count of fixed 1s seen thus far, q = count of ? seen thus far
ones,q = 0,0
for char in seq:
    if char == "0":
        A += ones
        B += q
    elif char == "1":
        ones += 1
    else: # question mark
        q += 1
        k += 1
        B += ones
C = (k * (k - 1)) >> 1
P = pow(2,k,M)
ans = P * (A % M)
ans += P * inv2 % M * (B % M)
ans += P * inv2 % M * inv2 % M * (C % M)
print(ans % M)
