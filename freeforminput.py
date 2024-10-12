from sys import stdin,stdout

for line in stdin:
    line = line.strip()
    num,total = [],0
    for char in line:
        if char == ",":
            n = float("".join(num))
            total += n
            num = []
        elif char != " ":
            num.append(char)
    if num:
        n = float("".join(num))
        total += n
        num = []
    stdout.write(f"{total}\n")
