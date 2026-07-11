from sys import stdin
from heapq import heappush,heappop,heapify

def solve(nums):
    while len(nums) > 1:
        a = heappop(nums)
        if nums and nums[0] == a:
            heappop(nums)
            heappush(nums,a << 1)
    return nums[0]
    
stdin.readline()
nums = list(map(int,stdin.readline().split()))
heapify(nums)
print(solve(nums))
