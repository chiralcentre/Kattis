def distance_squared(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

while True:
    d,N = input().split()
    d,N = float(d),int(N)
    if d == 0.0 and N == 0:
        break
    sour_hives = set()
    hives = [tuple(map(float,input().split())) for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            if distance_squared(hives[i],hives[j]) <= d**2:
                sour_hives.add(hives[i])
                sour_hives.add(hives[j])
    print(f'{len(sour_hives)} sour, {N - len(sour_hives)} sweet')
                
