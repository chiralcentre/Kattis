from sys import stdin

n = int(stdin.readline())
if n == 0:
    print(f"*0")
else:
    nums = list(map(int,stdin.readline().split()))
    ans = nums[0]
    for i in range(1,len(nums)):
        ans = ans ^ nums[i] # take XOR of all numbers
    print(f"*{ans}")
