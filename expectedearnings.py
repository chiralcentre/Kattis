line = input().split()
n,k,p = int(line[0]),int(line[1]),float(line[2])
print("spela") if (n-k)*p+(-k)*(1-p) < 0 else print("spela inte!")
