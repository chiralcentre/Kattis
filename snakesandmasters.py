from sys import stdin,stdout

def solution(n): #O(n) through bottom up DP
    # 1 way to take 0 steps, 1 way to take 1 step
    arr = [1,1] #memoisation
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]%(10**6)

stdout.write(str(solution(int(stdin.readline()))))
