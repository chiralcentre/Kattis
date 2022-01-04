print(sum([(lambda x: x[0]*x[1])(tuple(map(float,input().split()))) for _ in range(int(input()))]))
