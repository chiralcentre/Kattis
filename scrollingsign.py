from sys import stdin,stdout

for i in range(int(stdin.readline())):
    k,w = map(int,stdin.readline().split())
    prev,counter = stdin.readline().strip(),k
    for j in range(w-1): #time complexity does not matter since k and w are small
        current = stdin.readline().strip()
        cursor1,cursor2 = 0,k
        while prev[cursor1:] != current[:cursor2]:
            cursor1 += 1; cursor2 -= 1
            counter += 1
        prev = current
    stdout.write(f"{counter}\n")
        
