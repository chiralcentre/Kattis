from sys import stdin,stdout

n = int(stdin.readline())
words = stdin.readline().split()
abbrev = [w[0] for w in words if w[0].isupper()]
stdout.write("".join(abbrev))
