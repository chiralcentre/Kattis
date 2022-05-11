from sys import stdin,stdout

lower,higher,honest = 0,11,True
while True:
    number = int(stdin.readline())
    if number == 0:
        break
    response = stdin.readline().strip()
    if response == "right on":
        stdout.write("Stan may be honest\n") if lower < number < higher and honest else stdout.write("Stan is dishonest\n")
        lower,higher,honest = 0,11,True #reset
    elif response == "too high":
        higher = min(higher,number) #take the tighter upper bound
    elif response == "too low":
        lower = max(lower,number) #take the tighter lower bound
            
    
