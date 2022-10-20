from sys import stdin,stdout

def withinBox(x1,y1,size,boxes):
    for a,b,c,d,s in boxes:
        if a <= x1 <= c and b <= y1 <= d:
            return f"{size} correct" if size == s else f"{size} {s}"
    return f"{size} floor"

first = True  
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    if first:
        first = False
    else:
        stdout.write("\n")
    boxes = []
    for i in range(n):
        *coords,size = stdin.readline().split()
        x1,y1,x2,y2 = map(float,coords)
        boxes.append((x1,y1,x2,y2,size))
    for i in range(int(stdin.readline())):
        *coords,size = stdin.readline().split()
        x1,y1 = map(float,coords)
        stdout.write(withinBox(x1,y1,size,boxes) + "\n")
