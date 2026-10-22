from sys import stdin,stdout

H = pow(10,6)
T,M = map(int,stdin.readline().split())
fact = [1 for _ in range(H + 1)]
for i in range(2,H + 1):
    fact[i] = (fact[i - 1] * i) % M
inv = [1,1]
# let I(N) be the number of involutions on N elements
# looking at the last element N - 1, there are two cases
# case 1: leave it fixed. Then, the rest is an involution on the other N - 1 elements
# case 2: pair ir with some other element (N - 1) choices. Remaining elements must form an involution amongst themselves
for i in range(H):
    inv.append((inv[-1] + (len(inv) - 1) * inv[-2]) % M)
for _ in range(T):
    N = int(stdin.readline())
    stdout.write(f"{(fact[N] - inv[N] + M) % M}\n")
