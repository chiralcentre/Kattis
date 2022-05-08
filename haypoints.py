from sys import stdin,stdout

m,n = map(int,stdin.readline().split())
words = {}
for i in range(m):
    a,value = stdin.readline().split()
    words[a] = int(value)
for j in range(n):
    counter = 0
    while True:
        line = stdin.readline().split()
        if line:
            if line[0] != '.':
                for w in line:
                    if w in words:
                        counter += words[w]
            else:
                break
    stdout.write(f'{counter}\n')
    
