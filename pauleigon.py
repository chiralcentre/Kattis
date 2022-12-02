print((lambda x: "opponent" if ((int(x[1]) + int(x[2]))//int(x[0]))%2 else "paul")(tuple(map(int,input().split()))))
