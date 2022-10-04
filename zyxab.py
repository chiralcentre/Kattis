from sys import stdin,stdout

n = int(stdin.readline())
names = []
for _ in range(n):
    word = stdin.readline().strip()
    unique = set(word)
    if len(unique) == len(word) and len(word) >= 5:
        names.append(word)
if not names:
    stdout.write("neibb!")
else:
    #sort by length in descending order and lexicographical order in ascending order
    names.sort(key = lambda x: (-len(x),x))
    stdout.write(names[-1])
