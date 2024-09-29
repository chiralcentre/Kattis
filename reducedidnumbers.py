from sys import stdin

def solve(nums):
    for i in range(1, H + 1):
        rems = {x % i for x in nums}
        if len(rems) == G:
            return i
    return -1 # not supposed to happen

# code runs in O(GH) time, where H is maximum SIN
G = int(stdin.readline())
H = pow(10,6) - 1
nums = [int(stdin.readline()) for _ in range(G)]
print(solve(nums))
