#the recursive solution only works if times is sorted
def solution(times,N):
    if N < 3:
        return times[N-1] #only cross once
    elif N == 3:
        return times[0]+times[1]+times[2] #every person is accounted for
    else:
        #t1 refers to the time taken to move times[N-1] and times[0] across, move times[0] back, and move times[N-2] and times[0] across
        #t2 refers to the time taken to move times[N-1] and times[1] across, move times[1] back, and move times[1] and times[0] across
        t1 = times[N-1] + times[0] + times[N-2] + times[0]
        t2 = times[1] + times[0] + times[N-1] + times[1]
        if t1 < t2:
            return t1 + solution(times,N-2)
        else:
            return t2 + solution(times,N-2)

N,*group = map(int,input().split())
group.sort()
print(solution(group,N))

