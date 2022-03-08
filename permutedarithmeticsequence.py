from sys import stdin,stdout

def arithmetic(lst,n):
    d = lst[1] - lst[0]
    for i in range(2,n):
        if lst[i] - lst[i-1] != d:
            return False
    return True

for _ in range(int(stdin.readline())):
    m,*numbers = list(map(int,stdin.readline().split()))
    if arithmetic(numbers,m):
        stdout.write("arithmetic\n")
    else:
        stdout.write("permuted arithmetic\n") if arithmetic(sorted(numbers),m) else stdout.write("non-arithmetic\n")
