from sys import stdin,stdout

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0 for _ in range(4 * self.n)]
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2

            self.build(arr, left, start, mid)
            self.build(arr, right, mid + 1, end)

            self.tree[node] = min(self.tree[left], self.tree[right])

    def query(self, node, start, end, l, r):
        # no overlap
        if r < start or end < l:
            return float('inf')

        # total overlap
        if l <= start and end <= r:
            return self.tree[node]

        # partial overlap
        mid = (start + end) // 2
        left_min = self.query(2 * node + 1, start, mid, l, r)
        right_min = self.query(2 * node + 2, mid + 1, end, l, r)

        return min(left_min, right_min)

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = min(self.tree[2 * node + 1],
                                  self.tree[2 * node + 2])

N,Q = map(int,stdin.readline().split())
st = SegmentTree([0 for _ in range(N)])
for _ in range(Q):
    op,a,b = stdin.readline().split()
    if op == "Q":
        a,b = int(a) - 1,int(b) - 1
        stdout.write(f"{st.query(0,0,N - 1,a,b)}\n")
    else:
        a,b = int(a) - 1,int(b)
        st.update(0,0,N - 1,a,b)
