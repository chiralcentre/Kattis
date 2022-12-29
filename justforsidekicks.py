from sys import stdin,stdout

class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0 for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            j = i + self.lsone(i)
            if j <= self.n:
                self.ft[j] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    def select(self, k):
        p = 1
        while p << 1 <= self.n: p <<= 1
        i = 0
        while p > 0:
            if k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p
            p >>= 1
        return i + 1
    
N,Q = map(int,stdin.readline().split())
values = list(map(int,stdin.readline().split()))
gems = list(stdin.readline().strip())
arr = [[],[],[],[],[],[]]
#construct frequency array for every gem type in O(N) time
for char in gems:
    for i in range(6):
        arr[i].append(1) if i == int(char) - 1 else arr[i].append(0)
#construct 6 Fenwick trees, one for each gem type
trees = [FTree(arr[i]) for i in range(6)]
for i in range(Q):
    line = stdin.readline().split()
    a,b = int(line[1]) - 1,int(line[2]) - 1
    if line[0] == "1":
        old = int(gems[a]); old -= 1
        trees[old].update(a + 1, -1)
        trees[b].update(a + 1,1)
        gems[a] = b + 1
    elif line[0] == "2":
        values[a] = b + 1
    elif line[0] == "3":
        cf = [trees[i].query(a + 1, b + 1) for i in range(6)]
        stdout.write(f"{sum(values[i]*cf[i] for i in range(6))}\n")
            
