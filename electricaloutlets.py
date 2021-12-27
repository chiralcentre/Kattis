for i in range(int(input())):
    power_strips = list(map(int,input().split()))[1:]
    print(sum(power_strips)-len(power_strips)+1)
