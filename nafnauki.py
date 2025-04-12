def solve():
    string = input().strip()
    for i in range(len(string) - 1, -1, -1):
        if string[i] == ".":
            return string[i:]

if __name__ == "__main__":
    print(solve())