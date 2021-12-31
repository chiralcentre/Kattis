def rotate90Clockwise(m):
    matrix = []
    for i in range(len(m[0])):
        lst = []
        for j in range(len(m)-1,-1,-1):
            if m[j][i] == '+' or m[j][i] == ' ':
                lst.append(m[j][i])
            else:
                lst += ['|'] if m[j][i] == '-' else ['-']
        matrix.append(lst)
    return matrix
    
first = False
while True:
    n = int(input())
    if n == 0:
        break
    if first:
        print() # a new line between adjacent figures
    first = True
    image,longest = [],0
    for i in range(n):
        line = list(input().rstrip())
        image.append(line)
        if len(line) > longest:
            longest = len(line)
    for row in image:
        row += [' ']*(longest-len(row))
    for row in rotate90Clockwise(image):
        print(''.join(row).rstrip()) #rstrip to remove spaces
    

