def firstpersistent(num):
    factors = []
    switch = True
    while num >= 10:
        divided = False
        for i in range(9,2,-1):
            if not num%i: # keep dividing by highest factor
                divided = True
                num //= i
                factors.append(i)
                break
        if not divided: # has prime factor higher than 10
            switch = False
            break
    factors.append(num) #left over number 
    return ''.join(map(str,sorted(factors))) if switch else "There is no such number."
            
while True:
    n = int(input())
    if n == -1:
        break
    print(n + 10) if n < 10 else print(firstpersistent(n))
        
    
