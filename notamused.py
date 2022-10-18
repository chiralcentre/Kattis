from sys import stdin,stdout

days,entered,cost = 0,{},{}
for line in stdin:
    line = line.split()
    if line[0] == "OPEN":
        if days > 0: stdout.write("\n") #blank line between consecutive reports
        days += 1
        stdout.write(f"Day {days}\n")
    elif line[0] == "ENTER":
        entered[line[1]] = int(line[2]) / 10
    elif line[0] == "EXIT":
        cost[line[1]] = int(line[2]) / 10 - entered[line[1]] if line[1] not in cost else cost[line[1]] + int(line[2]) / 10 - entered[line[1]] 
        entered.pop(line[1]) #remove from dictionary
    else:
        for key,value in sorted(cost.items(),key = lambda x: x[0]):
            rounded = "{:.2f}".format(value)
            stdout.write(f"{key} ${rounded}\n")
        entered,cost = {},{} #reset
        
        
