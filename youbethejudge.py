from sys import stdin

# code taken from PyRival library
def is_prime(n):
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True
def solve():
    nums = []
    for line in stdin:
        line = line.strip().split()
        for n in line:
            try:
                nums.append(int(n))
                if str(int(n)) != n:
                    raise Exception
            except:
                return False
    return (len(nums) == 3 and
            nums[0] == nums[1] + nums[2] and
            nums[0] % 2 == 0 and
            3 < nums[0] <= pow(10,9) and
            is_prime(nums[1]) and
            is_prime(nums[2])
            )

print(int(solve()))
