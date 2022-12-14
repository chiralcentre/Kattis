from sys import stdin,stdout

def explode(K,N):
    counter = 210 # 3 minutes 30 seconds
    for i in range(N):
        time,answer = stdin.readline().split()
        counter -= int(time)
        if counter <= 0:
            return str(K)
        if answer == 'T':
            K = 1 if K == 8 else K + 1 #8 players
    return K
    
K,N = int(stdin.readline()), int(stdin.readline())
stdout.write(explode(K,N)+'\n')
