from sys import stdin,stdout

def shoelaceformula(x,y): #assuming coordinates of first point have been added, asusme anticlockwise
    return sum(x[i]*y[i+1] - y[i]*x[i+1] for i in range(len(x)-1))/2

# assume we start at 0,0
x,y = [0],[0]
N = int(stdin.readline())
movements = stdin.readline().split()
for pair in movements:
    m,d = pair[0],int(pair[1:])
    cx,cy = x[-1],y[-1]
    if m == "N":
        cx += d
    elif m == "E":
        cy += d
    elif m == "S":
        cx -= d
    else:
        cy -= d
    x.append(cx)
    y.append(cy)
x.append(0)
y.append(0)
print(f"THE AREA IS {abs(int(shoelaceformula(x,y)))}\n")
    
