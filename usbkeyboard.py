from sys import stdin

s = stdin.readline().strip()
reports,i = 0,0
while i < len(s):
    reports += 1
    count = 1
    # strictly increasing: same key can't be pressed twice in one report
    while i + count < len(s) and count < 6 and s[i + count] > s[i + count - 1]:
        count += 1
    i += count
print(reports)
