for _ in range(int(input())):
    stores = int(input())
    print((lambda x: 2*(max(x) - min(x)))(list(map(int,input().split()))))
