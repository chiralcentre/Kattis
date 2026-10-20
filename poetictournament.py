from sys import stdin
from heapq import heappop,heappush,heapify

def query(a, b):
    # returns True if a < b
    print(f"? {a} {b}", flush = True)
    return int(stdin.readline()) == b

class Applicant:
    memo = {}
    def __init__(self, idx):
        self.idx = idx
    def __lt__(self, other):
        a,b = sorted((self.idx, other.idx))
        key = (a, b)
        if key not in Applicant.memo:
            res = query(self.idx, other.idx)
            Applicant.memo[key] = res if self.idx < other.idx else not res
        return Applicant.memo[key] if self.idx < other.idx else not Applicant.memo[key]

N,K = map(int,stdin.readline().split())
best = []
for i in range(1, min(K + 1, N + 1)):
    best.append(Applicant(i))
heapify(best)
for i in range(K + 1, N + 1):
    A = Applicant(i)
    heappush(best,A)
    heappop(best)
print("! " + " ".join(str(a.idx) for a in best), flush = True)
