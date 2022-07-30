from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
heights = list(map(int,stdin.readline().split()))
#time complexity of naive approach is O(N*max_height)
#binary search can reduce time complexity to O(N*log(max_height))
#if a height of A has been tried and it cuts off less than M metres of wood, H < A.
#if a height of A has been tried and it cuts off at least M metres of wood. H >= A.
low,mid,high = 0,0,max(heights)
sol = -1
while low <= high:
    mid = (high + low) // 2
    cutoff = sum(h - mid for h in heights if h > mid)
    if cutoff < M:
        high = mid - 1
    else:
        low = mid + 1
        sol = mid
stdout.write(str(sol))
