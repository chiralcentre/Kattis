def collatz(N):
    counter = 1
    while N != 1:
        N = 3*N+1 if N%2 else N//2
        counter += 1
    return counter

print(collatz(int(input())))
