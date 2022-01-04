def harshadnumber(n):
    digit_sum = sum(list(map(int,list(str(n)))))
    return False if n%digit_sum else True

n = int(input())
while not harshadnumber(n):
    n += 1
print(n)
