from sys import stdin
from itertools import combinations

def check_suitability(comb, problems, k):
    contest_topics = {}
    for idx in comb:
        topics = problems[idx]
        for t in topics:
            contest_topics[t] = contest_topics.get(t, 0) + 1
            if contest_topics[t] > (k >> 1):
                return 0
    return 1

# code runs in O(NCk * max_t * k)
n,k = map(int,stdin.readline().split())
problems = []
for i in range(n):
    _,*topics = stdin.readline().split()
    problems.append(set(topics))

indices,ans = [i for i in range(n)],0
for comb in combinations(indices,k):
    ans += check_suitability(comb, problems, k)
print(ans)
