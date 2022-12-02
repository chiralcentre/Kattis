from sys import stdin,stdout

minutes,seconds = 0,0
for _ in range(int(stdin.readline())):
    M,S = map(int,stdin.readline().split())
    minutes += M; seconds += S
stdout.write("measurement error") if minutes * 60 >= seconds else stdout.write(f"{seconds/(minutes*60)}")
   
