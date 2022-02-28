n = int(input())
distances = list(map(int,input().split()))
people = ['1' for _ in range(n)]
for i in range(n-1):
    people[distances[i]+1] = str(i+2)
print(' '.join(people))
