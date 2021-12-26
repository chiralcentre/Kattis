for i in range(int(input())):
    K,N = list(map(int,input().split()))
    print(f'{K} {(N**2 + 3*N)//2}')
