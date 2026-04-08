from sys import stdin

n = int(stdin.readline())
nums = sorted(map(int,stdin.readline().split()))
print(nums[n // 2]) if n % 2 else print((nums[n // 2 - 1] + nums[n // 2]) / 2)
