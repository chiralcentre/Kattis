from sys import stdin,stdout

data = [line for line in stdin]
stdout.write(f"{len(data)}\n")
for line in data:
    stdout.write(line)