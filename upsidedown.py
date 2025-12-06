from sys import stdin,stdout

n = int(stdin.readline())
words = sorted(map(lambda x: x[::-1], stdin.readline().split()), reverse = True)
stdout.write(" ".join(w for w in words))
