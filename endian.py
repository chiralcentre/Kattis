from sys import stdin

stdin.readline() # from and to endian types not required, assuming they always differ
N = int(stdin.readline())
line = stdin.readline().strip()
encoding,seq = line[0:2],line[2:]
output = []
step = 8 if encoding == "0b" else 2
end = N if encoding == "0b" else N >> 2
for i in range(0,end,step):
    output.append(seq[i:i+step])
print(f"{encoding}{''.join(output[::-1])}")
