from sys import stdin,stdout

FINAL_LINE = "*" * 4 + " " * 76
N,M,S,T = stdin.readline().split()
N,M = int(N),int(M)
translation = {S[i]: T[i] for i in range(M)}
output = []
for line in stdin:
    line = line.strip("\n")
    if line == FINAL_LINE:
        break
    temp,consec = [],0
    for char in line:
        if char in translation:
            if consec >= 4:
                temp.append(f"&{str(consec).zfill(2)}")
            else:
                for i in range(consec):
                    temp.append(" ")
            consec = 0
            temp.append(translation[char])
        elif char == " ":
            consec += 1
        else:
            if consec >= 4:
                temp.append(f"&{str(consec).zfill(2)}")
            else:
                for i in range(consec):
                    temp.append(" ")
            consec = 0
            temp.append(char)
            consec = 0
    if consec >= 4:
        temp.append(f"&{str(consec).zfill(2)}")
    else:
        for i in range(consec):
            temp.append(" ")
    output.append("".join(temp))

s = 0
while s < len(output):
    k = s
    total = len(output[s])
    while s + 1 < len(output) and total + len(output[s + 1]) <= N:
        s += 1
        total += len(output[s])
    for i in range(k,s + 1):
        stdout.write(output[i])
    stdout.write("\n")
    s += 1
