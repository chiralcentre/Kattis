from sys import stdin,stdout

for line in stdin:
    a,op,b = line.split()
    if op == '+': # add last four digits together
        stdout.write(f'{(int(a[-4:])+int(b[-4:]))%10000}\n')
    elif op == '*': #multiply last four digits together
        stdout.write(f'{(int(a[-4:])*int(b[-4:]))%10000}\n')
    else: #O(log(b)) mulltiplications
        stdout.write(f'{pow(int(a),int(b),10000)}\n')
