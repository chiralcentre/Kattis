from sys import stdin

ans = 0
for _ in range(int(stdin.readline())):
    num = stdin.readline().strip()
    if num.startswith("+39") and 12 <= len(num) <= 13:
        ans += 1
print(ans)
