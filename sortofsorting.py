first = True
while True:
    n = int(input())
    if n == 0:
        break
    if not first:
        print() #newline
    else:
        first = False
    names = [input().strip() for _ in range(n)]
    #Python's sorted function is stable
    print('\n'.join(sorted(names,key = lambda x: (x[0],x[1]))))
