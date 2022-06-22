from sys import stdin,stdout
from math import ceil
#convert octal to binary first, as octal digits correspond to three binary digits
#hex digit correspond to four binary digits

hexadecimal = {('0','0','0','0'):'0', ('0','0','0','1'):'1', ('0','0','1','0'):'2', ('0','0','1','1'):'3',
               ('0','1','0','0'):'4', ('0','1','0','1'):'5', ('0','1','1','0'):'6', ('0','1','1','1'):'7',
               ('1','0','0','0'):'8', ('1','0','0','1'):'9', ('1','0','1','0'):'A', ('1','0','1','1'):'B',
               ('1','1','0','0'):'C', ('1','1','0','1'):'D', ('1','1','1','0'):'E', ('1','1','1','1'):'F',}

number = stdin.readline().strip()
binary = []
numdigits = ceil(3*len(number)/4)*4 #include leading zeroes to make up to a multiple of four
for i in range(numdigits-3*len(number)):
    binary.append('0')

for digit in number:
    n = int(digit)
    triplet = []
    while n >= 1:
        rem = n%2
        n //= 2
        triplet.append(str(rem))
    # include leading zeroes if there is not enough digits to make up to three digits
    for i in range(3-len(triplet)):
        triplet.append("0")
    # the order of the digits in triplet are in reverse
    for i in range(2,-1,-1):
        binary.append(triplet[i])

#convert binary to hexadecimal by grouping every 4 binary digits
if len(binary) == 4: # a zero as the leading digit is only acceptable if it is the only digit
    stdout.write(hexadecimal[(binary[0],binary[1],binary[2],binary[3])])
else:
    if hexadecimal[(binary[0],binary[1],binary[2],binary[3])] != '0': # no leading zeroes allowed
        stdout.write(hexadecimal[(binary[0],binary[1],binary[2],binary[3])])
    for i in range(4,len(binary),4):
        a,b,c,d = binary[i],binary[i+1],binary[i+2],binary[i+3]
        stdout.write(hexadecimal[(a,b,c,d)])
    


