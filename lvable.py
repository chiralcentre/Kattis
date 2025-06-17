# maximum two moves are required
def solve(s):
    if "lv" in s:
        return 0
    letters = set(s)
    if "l" in s or "v" in s:
        return 1
    return 2

if __name__ == "__main__":
    input()
    s = input().strip()
    print(solve(s))
