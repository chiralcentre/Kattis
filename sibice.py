N,W,H = map(int,input().split())
longest_length_squared = W**2 + H**2 #can place as the hypotenuse

for _ in range(N):
    print('DA') if int(input())**2 <= longest_length_squared else print('NE')
