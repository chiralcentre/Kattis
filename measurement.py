from sys import stdin,stdout

conversion = [1, 1000, 12, 3, 22, 10, 8, 3]
table = {
    'thou': 0, 'th': 0,
    'inch': 1, 'in': 1,
    'foot': 2, 'ft': 2,
    'yard': 3, 'yd': 3,
    'chain': 4, 'ch': 4,
    'furlong': 5, 'fur': 5,
    'mile': 6, 'mi': 6,
    'league': 7, 'lea': 7
}

line = stdin.readline().split()
v,u1,u2 = int(line[0]),line[1],line[3]
start,end = table[u1],table[u2]
if start < end:
    start += 1
    while start <= end:
        v /= conversion[start]
        start += 1
else:
    while start > end:
        v *= conversion[start]
        start -= 1
        
stdout.write(f'{v}\n')
