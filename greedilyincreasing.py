from sys import stdin,stdout

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
GIS,smallest = [str(A[0])],A[0]
for i in range(1,N):
    if A[i] > smallest:
        GIS.append(str(A[i]))
        smallest = A[i]
stdout.write(f'{len(GIS)}\n')
stdout.write(' '.join(GIS)+'\n')
