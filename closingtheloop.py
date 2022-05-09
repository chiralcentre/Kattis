from sys import stdin,stdout

for i in range(int(stdin.readline())):
    S = int(stdin.readline())
    blue,red = [],[]
    segments = stdin.readline().split()
    for s in segments:
        blue.append(int(s[:-1])) if s[-1] == 'B' else red.append(int(s[:-1]))
    blue.sort(); red.sort()
    counter = 0; connections = 0
    while blue and red: #colour alternation possible
        counter += blue.pop() + red.pop()
        connections += 1
    stdout.write(f'Case #{i+1}: {counter - 2*connections}\n') #subtract by 2 times the number of connections
