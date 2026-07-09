from sys import stdin,stdout

# precondition: 1 <= T <= 400
def get_sym(T):
    if T <= 80:
        return "K"
    elif T <= 160:
        return "k"
    elif T <= 240:
        return "."
    elif T <= 320:
        return "h"
    else:
        return "H"
    
h,w = int(stdin.readline()),int(stdin.readline())
for i in range(h):
    for j in range(w):
        _,_,t = map(int,stdin.readline().split())
        stdout.write(get_sym(t))
    stdout.write("\n")
