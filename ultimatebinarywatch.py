from collections import deque

def decimalToBinary(num):
    binary = deque([])
    while num >= 1:
        binary.appendleft(str(num%2))
        num //= 2
    if len(binary) < 4: # clock format
        for i in range(4-len(binary)):
            binary.appendleft('0')
    return binary

time = list(input().strip())
matrix = [[' ' for i in range(9)] for j in range(4)]
for k in range(4):
    binarytime = decimalToBinary(int(time[k]))
    for m in range(4):
        if k < 2:
            matrix[m][2*k] = '.' if binarytime[m] == '0' else '*'
        else:
            matrix[m][2*k+2] = '.' if binarytime[m] == '0' else '*'
            
print('\n'.join(''.join(row) for row in matrix))
