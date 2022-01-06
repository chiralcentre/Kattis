while True:
    n = int(input())
    if n == -1:
        break
    distance,prev = 0,0
    for _ in range(n):
        s,t = map(int,input().split())
        distance += s*(t-prev)
        prev = t
    print(f'{distance} miles')
