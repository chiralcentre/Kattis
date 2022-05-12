from sys import stdin,stdout

N,Y = map(int,stdin.readline().split())
found = [False for _ in range(N)]; counter = 0
for i in range(Y):
    a = int(stdin.readline())
    if not found[a]:
        found[a] = True
        counter += 1
stdout.write('\n'.join(str(i) for i in range(N) if not found[i])+'\n')
stdout.write(f'Mario got {counter} of the dangerous obstacles.\n')
