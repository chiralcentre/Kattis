W = int(input())
total_area = sum((lambda x: int(x[0])*int(x[1]))(input().split()) for _ in range(int(input())))
print(total_area//W)
