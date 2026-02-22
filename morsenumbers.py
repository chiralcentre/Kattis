T = {"0": 19, "1": 17, "2": 15, "3": 13,
     "4": 11, "5": 9, "6": 11, "7": 13,
     "8": 15, "9": 17}
N = int(input())
nums = input().strip().split()
ans = 0
for num in nums:
    for d in num:
        ans += T[d]
    ans += (len(num) - 1) * 3
ans += 7 * (len(nums) - 1)
print(ans)
