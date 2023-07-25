from sys import stdin,stdout

# precompute factorials
fact = [1]
for i in range(49):
    fact.append(fact[-1] * (i + 1))

# k can exceed long data type
for line in stdin:
    n,k = map(int,line.split())
    perm = [i + 1 for i in range(n)]
    ans = []
    while n > 0: # O(n^2) approach
        a = perm[k // fact[n - 1]]
        ans.append(a)
        k %= fact[n - 1]
        n -= 1
        perm.remove(a)
    stdout.write(" ".join(str(p) for p in ans))
    stdout.write("\n")
