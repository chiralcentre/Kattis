N,P,S = map(int,input().split())
for _ in range(S):
    line = list(map(int,input().split()))
    cards = line[1:]
    print('KEEP') if P in cards else print('REMOVE')
    
