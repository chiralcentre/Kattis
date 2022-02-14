for _ in range(int(input())):
    s,d = map(int,input().split())
    # sum of s + d must be even for the two scores to be integers
    print("impossible") if d > s or (s + d)%2 else print(f'{(s+d)//2} {(s-d)//2}')
        
