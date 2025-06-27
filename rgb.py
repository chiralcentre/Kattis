R,G,B,k = map(int,input().split())
C = B + G
# if there are moves but no more B or G, 1R -> 2C (1 move)
# 1R -> 2C -> 2R (3 moves)
# afterwards, its a self sustaining cycle
# for every move taking from either G or B, C remains constant and R += 1
if C == 0 and R > 0 and k > 2:
    k -= 2
    R += k 
elif C > 0: # C > 0
    R += k
print(R)
