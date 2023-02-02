def solve(total,t1,t2,t3,t4):
    #there are five possible insertion points of fifth time
    #case 1: new time is inserted before t1, and new time,t4 are discarded
    if t1 + t2 + t3 > total:
        return "impossible"
    #case 2: new time is inserted after t4, t1, new time are discarded
    if t2 + t3 + t4 <= total:
        return "infinite"
    #case 3: new time is inserted in between t1 and t2, t1,t4 are discarded
    #case 4: new time is inserted in between t2 and t3, t1,t4 are discarded
    #case 5: new time is inserted in between t3 and t4, t1,t4 are discarded
    return "{:.2f}".format((total - t2 - t3)/100)

#convert to integer to avoid floating point imprecision
t1,t2,t3,t4 = input().split()
e1,e2 = input().split(".")
p1,p2 = t1.split(".")
p3,p4 = t2.split(".")
p5,p6 = t3.split(".")
p7,p8 = t4.split(".")
t1 = int(p1) * 100 + int(p2)
t2 = int(p3) * 100 + int(p4)
t3 = int(p5) * 100 + int(p6)
t4 = int(p7) * 100 + int(p8)
total = int(e1) * 100 + int(e2)
total *= 3
t1,t2,t3,t4 = sorted([t1,t2,t3,t4])
print(solve(total,t1,t2,t3,t4))


