numbers = map(lambda x: x[::-1],input().split())
print(sorted(list(map(int,numbers)))[1])
