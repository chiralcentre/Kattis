m,a,b,c = map(int,input().split())
# minimum intersection between three sets is N(A) + N(B) + N(C) - 2N
print('possible') if a + b + c - 2*m <= 0 else print('impossible')
