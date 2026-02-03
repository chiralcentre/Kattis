from sys import stdin

n = int(stdin.readline())
students = sorted(map(int, stdin.readline().split()), reverse = True)
print(sum(pow(2, -i - 1) * students[i] for i in range(n)))
