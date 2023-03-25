from sys import stdin,stdout

def solve(s1):
    #sep = -1 means that the number of separating white pixels for first pair of black pixels has not been calculated yet
    sep,count = -1,0
    #start from second pixel, since first pixel is always black
    for i in range(1,len(s1)):
        if s1[i] == ".":
            count += 1
        else:
            if sep == -1 or count == sep:
                sep = count
                count = 0 #reset count
            else:
                return "NOT EVEN"
    return "EVEN"

counter = 1
while True:
    string = stdin.readline().strip()
    if string == 'END':
        break
    stdout.write(f'{counter} {solve(string)}\n')
    counter += 1
