from sys import stdin,stdout

def arithmetic_mean(seq):
    return sum(seq)/len(seq)

# take root first to avoid imprecision when taking root of very large number
def geometric_mean(seq):
    prod = 1
    for elem in seq:
        prod *= pow(elem, 1 / len(seq))
    return prod

# assume seq is sorted
def median(seq):
    return seq[(len(seq) + 1) // 2 - 1]

n = int(stdin.readline())
seq = sorted(map(float,stdin.readline().split()))
temp = sorted([arithmetic_mean(seq),geometric_mean(seq),median(seq)])
while temp[2] - temp[0] > 5 * pow(10,-6):
    temp = sorted([arithmetic_mean(temp),geometric_mean(temp),median(temp)])
print(format(arithmetic_mean(temp), '.8f'))
