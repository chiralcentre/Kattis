nums = sorted(list(map(int,input().split())))
# sum of AP with 4 terms
print(2*(2*nums[0] + 3*min(nums[1]-nums[0],nums[2]-nums[1]))-sum(nums))
    
