print((lambda x: (x[0] * pow(x[0] - 1, x[1] - 1)) % 998244353)(list(map(int,input().split()))))
