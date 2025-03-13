from sys import stdin,stdout

n = int(stdin.readline())
words = [[] for i in range(n)]
for i in range(n):
    _,*options = stdin.readline().split()
    words[i] = sorted(options)

spoilers = [[x] for x in words[0]]
for i in range(1, n):
    temp = []
    for s in spoilers:
        for w in words[i]:
            temp.append(s + [w])
    spoilers = temp
    
for lst in spoilers:
    stdout.write(" ".join(lst))
    stdout.write("\n")
