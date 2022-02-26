from sys import stdin,stdout

P = int(stdin.readline())
for _ in range(P):
    K,*students = list(map(int,stdin.readline().split()))
    steps = 0
    for i in range(1,20): # do bubble sort on students with O(N^2) time complexity
        isSorted = True
        for j in range(0,20-i):
            if students[j] > students[j+1]:
                students[j],students[j+1] = students[j+1],students[j]
                steps += 1
                isSorted = False
        if isSorted:
            break
    stdout.write(f'{K} {steps}\n')
