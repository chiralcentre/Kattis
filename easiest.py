import sys
# N is in string form
def digit_sum(N):
    return sum(int(digit) for digit in str(N))
for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    D,p = digit_sum(N),11
    while digit_sum(N*p) != D:
        p += 1
    print(p)
    
