from sys import stdin,stdout

H = -1
for _ in range(int(stdin.readline())):
    curr = stdin.readline().strip()
    if curr == "/":
        R = H + (10 - H % 10) if H % 10 else H + 10
        stdout.write(f"{R}\n")
    else:
        H = max(int(curr),H)
        stdout.write(f"{curr}\n")
