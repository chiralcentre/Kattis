def possiblecombination(n):
    num = str(n)
    unique_digits = set(num);
    if len(unique_digits) != len(num) or '0' in unique_digits:
        return False
    else:
        for divisor in unique_digits:
            if n%int(divisor):
                return False
        return True
            
L,H = map(int,input().split())
counter = 0
for i in range(L,H+1):
    if possiblecombination(i):
        counter += 1
print(counter)
    
