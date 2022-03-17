from sys import stdin,stdout

while True:
    line = stdin.readline().split()
    if line[0] == '0':
        break
    f,r = int(line[0]),int(line[1])
    front = list(map(int,stdin.readline().split())) 
    rear = list(map(int,stdin.readline().split()))
    #O(f*r + f*r log(f*r))
    drive_ratio = sorted([n/m for n in front for m in rear])
    maximum = -1 #O(f*r)
    for i in range(1,f*r):
        if drive_ratio[i]/drive_ratio[i-1] > maximum:
            maximum = drive_ratio[i]/drive_ratio[i-1]
    stdout.write('{0:.2f}'.format(maximum)+'\n')
