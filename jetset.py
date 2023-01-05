from sys import stdin,stdout

def solve():
    n = int(stdin.readline())
    waypoints = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
    intervals = []
    for i in range(n):
        l1,l2 = waypoints[i][1],waypoints[(i+1)%n][1]
        a,b = min(l1,l2),max(l1,l2)
        d = b - a
        if d == 180:
            return "yes" #passed through one of the poles
        if d < 360 + a - b: #goes directly from a to b
            intervals.append((a,b))
        else:
            intervals.append((-180,a))
            intervals.append((b,180))
    intervals.sort()
    #merge intervals
    stack = [intervals[0]]
    for i in range(1,len(intervals)):
        a,b = intervals[i]
        pa,pb = stack[-1]
        if pb >= a: #merge interval
            stack.pop()
            stack.append((pa,max(b,pb)))
        else: #cannot be merged, push new interval to stack
            stack.append((a,b))
        #print(f"step {i}")
        #print(stack)
    stack.sort()
    if stack[-1][1] != 180:
        return f"no 179.5"
    prev = -180
    for a,b in stack:
        if a > prev:
            return f"no {(a + prev)/2}"
        else:
            prev = b
    return "yes"

stdout.write(solve())



