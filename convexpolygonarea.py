for i in range(int(input())):
    polygon = list(map(int,input().split()))
    points = polygon[1:] + polygon[1:3]
    #shoelace formula
    counter = 0
    for i in range(0,len(points),2):
        if i + 3 in range(len(points)):
            counter += points[i]*points[i+3]
    for j in range(1,len(points),2):
        if j + 1 in range(len(points)):
            counter -= points[j]*points[j+1]
    print(counter/2)
        
