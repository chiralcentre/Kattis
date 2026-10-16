from sys import stdin

# overall approach runs in O(N^3)
N = int(stdin.readline())
S = sorted([int(stdin.readline()) for _ in range(N)])
# for every triple x,y,z, three inequalities must be fulfilled
# x + y > z, x + z > y, y + z > x (triangle inequality)
# WLOG, if x < y < z, we only need to focus on x + y > z, as the others are guaranteed by x < y < z
# given a subset with k elements, k >= 3, it is triangular iff smallest + second smallest > largest
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        # let c be the number of elements in the window (S[j],S[i] + S[j])
        # number of triangular subsets = 2^c - 1, since non empty subset does not count
        # c can be found in O(log N) time with binary search, but linear search will suffice here since N is small
        T = S[i] + S[j]
        c,p = 0,j + 1
        while p < N and S[p] < T:
            p += 1
            c += 1
        ans += pow(2,c) - 1
print(ans)
    
