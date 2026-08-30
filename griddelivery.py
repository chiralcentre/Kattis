from sys import stdin

# scan parcels in row major order
# maintain a list tails where tails[i] is column of last parcel picked up by driver i
# a driver whose tail is column t can take a newly scanned parcel at column c if t <= c (row is already <= new row by scan order)
# for a parcel of column c, among drivers with tails[i] <= c, give parcel to the one with largest such tail
# if no driver qualifies, hire a new driver starting at this parcel
# code runs in O(hw) time
h,w = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(h)]
# tails are kept in descending order
tails = []
for r in range(h):
    p = len(tails)
    for c in range(w):
        if grid[r][c] != 'C':
            continue
        # find i with largest tails[i] <= c
        while p > 0 and tails[p - 1] <= c:
            p -= 1
        if p == len(tails):
            tails.append(c)
        else:
            tails[p] = c
print(len(tails))
