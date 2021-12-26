def machines(C,K,socks):
    M,cap,i,j = 0,C,0,0
    while True:
        if not cap or socks[j] - socks[i] > K:
            M += 1
            cap = C
            i = j
        elif j < S - 1:
            j += 1
            cap -= 1
        else:
            return M + 1 #j == S - 1 which is end of socks list
    

S,C,K = list(map(int,input().split()))
socks = sorted(map(int,input().split()))
print(machines(C,K,socks))

         
