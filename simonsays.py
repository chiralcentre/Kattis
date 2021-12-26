num = int(input())
counter = 0

while counter < num:
    inpt = list(input().split())
    counter += 1
    if inpt[0] == 'Simon' and inpt[1] == 'says':
        string = ''
        for key,value in enumerate(inpt):
            if key == 0 or key == 1:
                continue
            else:
                string += value + ' '
        print(string)
    
