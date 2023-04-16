from sys import stdin,stdout

d,pt,ps = 0,0,0
for line in stdin:
    line = line.split()
    h,m,s = map(int,line[0].split(":"))
    t = h + ((60 * m + s)/ 3600)
    d += (t - pt) * ps
    if len(line) == 2: #change of speed
        ps = int(line[1])
    else: #query
        stdout.write(f"{line[0]} {d:.2f} km\n")
    pt = t
