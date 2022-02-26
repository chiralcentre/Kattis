from sys import stdin,stdout 
    
while True:
    line = stdin.readline().split()
    if len(line) == 1:
        break
    k,m = map(int,line)
    chosen = {course for course in stdin.readline().split()}
    meets_requirements = True
    for i in range(m):
        c,r,*courses = stdin.readline().split()
        taken = 0
        for course in courses:
            if course in chosen:
                taken += 1
        if taken < int(r):
            meets_requirements = False
    stdout.write('yes\n') if meets_requirements else stdout.write('no\n')
    
