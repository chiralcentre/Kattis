# find all possible powers of 2 that ends the CST
# maximum output is 2^47 * (3^25) / (2 ^ 25) ~= 2^62
# only 30 possible ending numbers
end = []
S,E = 16,pow(2,62)
while S <= E:
    if not (S - 1) % 3:
        end.append(S)
    S <<= 1
    
def check_valid(s):
    return s[-1] == "O" and "OO" not in s and set(s) == {"O","E"}

def test_valid_num(s,num):
    start = num
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "E":
            start <<= 1
        else:
            start -= 1
            if start % 3:
                return -1
            start //= 3
    return start

def solve(s):
    for num in end:
        res = test_valid_num(s,num)
        if res != -1: # answer is guaranteed if string is valid
            return res

string = input().strip()
print(solve(string)) if check_valid(string) else print("INVALID")

