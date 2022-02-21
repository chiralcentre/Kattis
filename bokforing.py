from sys import stdin,stdout

N,Q = map(int,stdin.readline().split())
base_value,different = '0',{}
for _ in range(Q):
    event = stdin.readline().split()
    if event[0] == 'SET':
        different[event[1]] = event[2]
    elif event[0] == 'RESTART':
        base_value = event[1]
        different.clear()
    else: #print command
        stdout.write(f'{different[event[1]]}\n') if event[1] in different else stdout.write(f'{base_value}\n') 
