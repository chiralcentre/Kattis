from sys import stdin,stdout

words = [stdin.readline().strip("\n") for _ in range(int(stdin.readline()))]
words.sort(key = lambda x: (x.lower(),x))
for w in words:
    stdout.write(f"{w}\n")
