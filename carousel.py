while True:
    n,m = list(map(int,input().split()))
    if n == 0 and m == 0:
        break
    dict1 = {}
    for i in range(n):
        a,b = list(map(int,input().split()))
        if a <= m:
            dict1[(a,b)] = b/a
    pair = ()
    for key,value in dict1.items():
        if value == min(dict1.values()):
            if not pair:
                pair = key
            elif key[0] > pair[0]:
                pair = key
    print(f'Buy {pair[0]} tickets for ${pair[1]}') if pair else print('No suitable tickets offered')
    
            
