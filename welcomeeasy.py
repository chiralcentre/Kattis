from sys import stdin,stdout

TARGET = "welcome to code jam"
TARGET_LEN = len(TARGET)

def count_subsequences(text):
    dp = [0] * (TARGET_LEN + 1)
    dp[0] = 1
    for i in range(len(text)):
        for j in range(TARGET_LEN, 0, -1):
            if text[i] == TARGET[j-1]:
                dp[j] += dp[j - 1]
    return dp[TARGET_LEN]

T = int(stdin.readline())
for i in range(1, T + 1):
    text = stdin.readline().strip()
    result = count_subsequences(text)
    stdout.write(f"Case #{i}: {result:04}\n")
