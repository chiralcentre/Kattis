first = True
while True:
    names, n = [],int(input())
    if n == 0:
        break
    if not first:
        print() #newline
    else:
        first = False
    for _ in range(n):
        names.append(input().strip())
    #Python's sorted function is stable
    print('\n'.join(sorted(names,key = lambda x: (x[0],x[1]))))
