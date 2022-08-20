#number of horizontal cards is 1 + 2 + 3 + 4 + ... + h - 1 = h(h-1)/2
#number of diagonal cards is 2 + 4 + 6 + 8 + .. + 2h = h(h+1)
#total number of cards is (3h**2 + h)/2
#for total number of cards to be multiple of 4, 3h**2 + h should be divisible by 8
#h should be divisible by 8 or have a remainder of 5 modulo 8
print((lambda x: x + min(-x%8,(5-x)%8))(int(input())))
