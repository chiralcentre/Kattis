from sys import stdin,stdout

x = stdin.readline().strip().count("S")
y = stdin.readline().strip().count("S")
stdout.write("S(" * x * y)
stdout.write("0")
stdout.write(")" * x * y)
