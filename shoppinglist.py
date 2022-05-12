from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
common = set(stdin.readline().split()) #read in first line
for i in range(n-1):
    line = set(stdin.readline().split())
    common = common.intersection(line)
    if not common: #empty set
        break
stdout.write(f'{len(common)}\n')
stdout.write('\n'.join(item for item in sorted(common)))
