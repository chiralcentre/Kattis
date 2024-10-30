from sys import stdin,stdout

mappings = {}
for i in range(256):
    t = i << 1
    t &= 0b11111111
    res = i ^ t
    mappings[res] = i
    
n = int(stdin.readline())
message = list(map(int,stdin.readline().split()))
stdout.write(" ".join(str(mappings[b]) for b in message))
stdout.write("\n")
