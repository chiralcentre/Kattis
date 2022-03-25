from sys import stdin,stdout

personnel =  set()
for _ in range(int(stdin.readline())):
    move,name = stdin.readline().split()
    if move == "entry":
        if name in personnel:
            stdout.write(f'{name} entered (ANOMALY)\n')
        else:
            personnel.add(name)
            stdout.write(f'{name} entered\n')
    else: #exit
        if name in personnel:
            personnel.remove(name)
            stdout.write(f'{name} exited\n')
        else:
            stdout.write(f'{name} exited (ANOMALY)\n')
