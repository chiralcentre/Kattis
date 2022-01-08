def lowest_number(L,D,X):
    for i in range(L,D+1):
        digits_sum = sum(map(int,list(str(i))))
        if digits_sum == X:
            return i

def highest_number(L,D,X):
    for j in range(D,L-1,-1):
        digits_sum = sum(map(int,list(str(j))))
        if digits_sum == X:
            return j
    
L,D,X = [int(input()) for _ in range(3)]

print(lowest_number(L,D,X))
print(highest_number(L,D,X))
