string = input().strip()
T,C,G = 0,0,0

for card in string:
    if card == 'T':
        T += 1
    elif card == 'C':
        C += 1
    elif card == 'G':
        G += 1

print(T**2 + C**2 + G**2 + min(T,C,G)*7)

    
