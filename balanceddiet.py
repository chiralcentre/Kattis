from sys import stdin,stdout


#min partition problem
def findMinDiff(i,subsetSum):
    if dp[i][subsetSum] != -1:
        return dp[i][subsetSum]
    if i < 0:
        return abs(total - 2 * subsetSum)
    dp[i][subsetSum] = min(findMinDiff(i - 1,subsetSum + arr[i]),findMinDiff(i - 1, subsetSum))
    return dp[i][subsetSum]

#each test case runs in O(nW) time, where W is total sum of the can calories values
while True:
    N,*arr = map(int,stdin.readline().split())
    if N == 0:
        break
    total = sum(arr)
    dp = [[-1 for i in range(total + 1)] for j in range(N)]
    minDiff = findMinDiff(N - 1,0)
    stdout.write(f"{(total + minDiff) >> 1} {(total - minDiff) >> 1}\n")
