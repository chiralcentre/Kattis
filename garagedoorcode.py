from sys import stdin,stdout
from itertools import combinations

# code runs in O(N * NcK)
def generate_k_length_combs(code,K):
    ans = set()
    indices = [i for i in range(len(code))]
    for comb in combinations(indices,K):
        temp = sorted(comb)
        ans.add("".join(code[i] for i in temp))
    return ans
        
K,N = map(int,stdin.readline().split())
common = generate_k_length_combs(stdin.readline().strip(),K)
for i in range(N - 1):
    res = generate_k_length_combs(stdin.readline().strip(),K)
    common = common.intersection(res)
stdout.write(f"{len(common)}\n")
for code in sorted(common):
    stdout.write(f"{code}\n")
