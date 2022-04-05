from sys import stdin,stdout

while True: #O(tMN) where t is number of test cases
    N,M = map(int,stdin.readline().split())
    if N == M == 0:
        break
    # ignore source and destination as they are not required
    intervals = [(lambda x: (int(x[2]),int(x[2])+int(x[3])))(stdin.readline().split()) for _ in range(N)]
    for i in range(M):
        a,b = map(int,stdin.readline().split()); b += a
        counter = 0
        for start,end in intervals:
            if start <= a < end or start < b <= end or (a < start and b > end): #overlap
                counter += 1
        stdout.write(f'{counter}\n')
