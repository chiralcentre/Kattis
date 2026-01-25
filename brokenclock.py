from itertools import product
from sys import stdout

def generate(pattern):
    blanks = [i for i, c in enumerate(pattern) if c == '-']
    for bits in product('01', repeat=len(blanks)):
        s = list(pattern)
        for i, b in zip(blanks, bits):
            s[i] = b
        yield ''.join(s)
        
mappings = {"1110111": "0", "0010010": "1", "1011101": "2",
            "1011011": "3", "0111010": "4", "1101011": "5",
            "1101111": "6", "1010010": "7", "1111111": "8",
            "1111010": "9"}
pos = [[] for _ in range(6)]
for i in range(6):
    num = "".join(input().split())
    for x in generate(num):
        if x in mappings:
            pos[i].append(mappings[x])
for time in sorted(list(product(*pos))):
    H = time[0] + time[1]
    M = time[2] + time[3]
    S = time[4] + time[5]
    if int(H) < 24 and int(M) <= 59 and int(S) <= 59:
        stdout.write(f"{H}:{M}:{S}\n")

    
