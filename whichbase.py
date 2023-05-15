from sys import stdin,stdout

def getDecimalRepr(num,base):
    total = 0
    for i in range(len(num)):
        total += int(num[i]) * pow(base,len(num) - i - 1)
        if int(num[i]) >= base:
            return 0
    return total

for _ in range(int(stdin.readline())):
    K,S = stdin.readline().split()
    stdout.write(f"{K} {getDecimalRepr(S,8)} {getDecimalRepr(S,10)} {getDecimalRepr(S,16)}\n")
