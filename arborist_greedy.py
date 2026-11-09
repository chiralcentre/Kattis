# code runs in O(N log N) time
N,K = map(int, input().split())
pos = list(map(int, input().split()))
weights = list(map(int, input().split()))

# answer = 2 * N + 2 * max(x_trip) for all trips
light,heavy = [],[]
for i in range(N):
    if weights[i] == 20:
        light.append(pos[i])
    else: # weight of 40
        heavy.append(pos[i])
light.sort(reverse = True)
walk = sum(heavy)
step = 2 if K >= 40 else 1 # pair 2 20kg trees together if possible
for i in range(0,len(light),step):
    walk += light[i]
print(2 * N + 2 * walk)
