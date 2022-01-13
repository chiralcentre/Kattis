a1,b1,a2,b2 = map(int,input().split())
a3,b3,a4,b4 = map(int,input().split())
# both probabilitiy distributions are symmetric around the mean.
# Therefore it’s enough to compare the expected values of both probability distributions – compare the sum of both lines of input.
print('Gunnar') if a1 + b1 + a2 + b2 > a3 + b3 + a4 + b4 else print('Emma') if a1 + b1 + a2 + b2 < a3 + b3 + a4 + b4 else print('Tie')
