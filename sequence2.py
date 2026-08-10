from sys import stdout

a,b,c = 1,2,3
for _ in range(int(input())):
    stdout.write(f"{a}\n");
    d = a + b + c
    a = b
    b = c
    c = d