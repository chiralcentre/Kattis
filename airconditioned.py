#intervals need to be sorted first
intervals = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])
lowest = 0
while intervals:
    lowest += 1
    x = intervals.pop(0)
    #check for intersection between ranges
    while intervals and (x[0] <= intervals[0][0] <= x[1] or x[0] <= intervals[0][1] <= x[1]): #bracket is important so that right clauses are not evaluated if intervals is empty
        y = intervals.pop(0)
        x = (max(y[0],x[0]),min(y[1],x[1]))
print(lowest)
