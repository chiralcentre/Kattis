def delimiter(string,strlen):
    opening,closing = {'(':')','[':']','{':'}'},{')':'(',']':'[','}':'{'}
    parentheses = [] #operates as a stack
    for i in range(n):
        if string[i] in opening:
            parentheses.append(string[i])
        elif string[i] in closing: # closing parentheses
            # empty parentheses list or last parenthesis does not match 
            if not parentheses or parentheses.pop() != closing[string[i]]:
                return f'{string[i]} {i}'
    return 'ok so far'

n,string = int(input()),input().strip()
print(delimiter(string,n))
                
        
