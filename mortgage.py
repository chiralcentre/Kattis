from sys import stdin,stdout

while True:
    X,Y,N,r = stdin.readline().split()
    if X == Y == N == r == "0":
        break
    X,Y,N,r = float(X),float(Y),int(N),float(r) 
    #calculate amount of money remaining at end of nth month
    bal = X * pow(1 + (r / 1200), N * 12) - (1200 * Y * (pow(1 + (r / 1200), N * 12) - 1))/r if r != 0 else X - 12 * N * Y
    stdout.write("YES\n") if bal <= 0 else stdout.write("NO\n")
