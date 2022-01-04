for _ in range(int(input())):
    line = input().split()
    b,p = int(line[0]),float(line[1])
    print(f'{format(60/(p/(b-1)),".4f")} {format(60*b/p,".4f")} {format(60/(p/(b+1)),".4f")}')

    
