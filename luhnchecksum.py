from sys import stdin,stdout

def multiplyByTwo(digit):
    return (2*digit)%10 + 1 if digit >= 5 else 2*digit

def luhn(s):
    return "FAIL" if (sum(multiplyByTwo(int(s[i])) for i in range(len(s)-2,-1,-2))+ sum(int(s[j]) for j in range(len(s)-1,-1,-2)))%10 else "PASS"

for _ in range(int(stdin.readline())):
    stdout.write(luhn(stdin.readline().strip())+'\n')
