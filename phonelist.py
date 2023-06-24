from sys import stdin,stdout

def isConsistent(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1].startswith(nums[i]):
            return "NO"
    return "YES"

for _ in range(int(stdin.readline())):
    # sort numbers in lexicographical order, and check if the ith number is a prefix of the (i + 1)th number
    nums = sorted([stdin.readline().strip() for _ in range(int(stdin.readline()))])
    stdout.write(f"{isConsistent(nums)}\n")
