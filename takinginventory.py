from sys import stdin,stdout

n = int(stdin.readline())
quantities = {}
for i in range(n):
    s,c = stdin.readline().split()
    quantities[s] = quantities.get(s,0) + int(c)
for key,value in quantities.items():
    stdout.write(f"{key} {value // 64 + (value % 64 != 0)}\n")
    
