def digit_product(n):
    counter = 1
    while n > 0:
        digit = n%10
        if digit != 0:
            counter *= digit
        n //= 10
    return counter

def sifferprodukt(n):
    while n > 9:
        n = digit_product(n)
    return n
            
num = int(input())
print(sifferprodukt(num))
