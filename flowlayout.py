from sys import stdin,stdout

while True:
    m = int(stdin.readline())
    if m == 0:
        break
    w,h,cum_w,cum_h = 0,0,0,0
    while True:
        x,y = map(int,stdin.readline().split())
        if (x,y) == (-1,-1):
            break
        # check if I can place more blocks on current row
        if cum_w + x > m:
            h += cum_h
            w = max(w,cum_w)
            cum_h,cum_w = y,x
        else:
            cum_w += x
            cum_h = max(y,cum_h)
    if (cum_w,cum_h) != (0,0):
        w = max(w,cum_w)
        h += cum_h
    stdout.write(f"{w} x {h}\n")
