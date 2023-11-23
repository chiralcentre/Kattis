from sys import stdin

mappings = {int("111101101101111",2): 0, int("001001001001001",2): 1, int("111001111100111",2): 2,
            int("111001111001111",2): 3, int("101101111001001",2): 4, int("111100111001111",2): 5,
            int("111100111101111",2): 6, int("111001001001001",2): 7, int("111101111101111",2): 8,
            int("111101111001111",2): 9}

def solve(lines):
    digits = []
    # increment is 4 due to empty column between digits
    for i in range(0,len(lines[0]),4):
        code = []
        for j in range(5):
            for k in range(i,i + 3):
                code.append("1") if lines[j][k] == "*" else code.append("0")
        num = int("".join(code),2)
        if num not in mappings:
            return "BOOM!!"
        digits.append(str(mappings[num]))
    res = int("".join(digits))
    return "BOOM!!" if res % 6 else "BEER!!"

lines = [stdin.readline() for i in range(5)]
print(solve(lines))
