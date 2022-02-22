from sys import stdin,stdout

for linenum,line in enumerate(stdin):
    n,*case = list(map(int,line.split()))
    lowest,highest = case[0],case[0] 
    for i in range(1,n):
        if case[i] < lowest:
            lowest = case[i]
        if case[i] > highest:
            highest = case[i]
    stdout.write(f'Case {linenum+1}: {lowest} {highest} {highest-lowest}\n')
