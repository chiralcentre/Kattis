from sys import stdin,stdout
from math import log

def get_bits(year):
    return 2 ** ((year-1960)//10 + 2)

#n! <= 2**b - 1 where b is number of bits
#-> ln(n) + ln(n -1) + ... + ln(1) <= ln(2**b -1) < ln(2**b) = bln(2)
def get_factstone_rating(year):
    n = 1; LHS = 0
    RHS = get_bits(year)*log(2)
    while LHS <= RHS:
        n += 1
        LHS += log(n)
    return n - 1
    
for line in stdin:
    year = int(line)
    if year == 0:
        break
    stdout.write(f"{get_factstone_rating(year)}\n")
    

