def SSD(b,n):
    lst, counter = [], 0
    while n > 0:
        digit = n%b
        n //= b
        lst = [digit] + lst
    for num in lst:
        counter += num**2
    return counter

counter = int(input())
num = 0
while num < counter:
    num += 1
    inpt = list(map(int,input().split()))
    print(f'{inpt[0]} {SSD(inpt[1],inpt[2])}')
        
    
        
    
        
        

    
