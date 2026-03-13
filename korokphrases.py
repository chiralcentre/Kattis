from sys import stdin

unique = set()
for _ in range(int(stdin.readline())):
    unique.add(stdin.readline().strip())
print(len(unique))
