n,p = list(map(int,input().split()))
cars = sorted(list(map(int,input().split())))
distances = [p*(i+1) - (cars[i]-cars[0]) for i in range(n)]
print(max(distances))
