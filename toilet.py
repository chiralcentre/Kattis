from sys import stdin,stdout

string = stdin.readline().strip()
prev1,prev2,prev3 = string[0],string[0],string[0]
firstPolicyAdjustments,secondPolicyAdjustments,thirdPolicyAdjustments = 0,0,0
for i in range(1,len(string)):
    if string[i] != prev1:
        firstPolicyAdjustments += 1
    if string[i] != prev2:
        secondPolicyAdjustments += 1
    if string[i] != prev3:
        thirdPolicyAdjustments += 1
    prev1,prev2,prev3 = string[i],string[i],string[i]
    if prev1 != 'U':
        firstPolicyAdjustments += 1
        prev1 = 'U'
    if prev2 != 'D':
        secondPolicyAdjustments += 1
        prev2 = 'D'
        
stdout.write(f'{firstPolicyAdjustments}\n')
stdout.write(f'{secondPolicyAdjustments}\n')
stdout.write(f'{thirdPolicyAdjustments}\n')
    
