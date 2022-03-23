from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    toys = {}
    for i in range(int(stdin.readline())):
        name,amount = stdin.readline().split()
        toys[name] = int(amount) if name not in toys else toys[name]+int(amount)
    stdout.write(f'{len(toys)}\n')
    for key,value in sorted(toys.items(),key = lambda x: (-x[1],x[0])): # sort by descending order of toy count, then break ties in ascending order of name
        stdout.write(f'{key} {value}\n')
