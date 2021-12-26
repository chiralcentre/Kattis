n = int(input())

for i in range(n):
    stops = int(input())
    passengers = 0
    for j in range(stops):
        passengers = 2*passengers + 1
    print(passengers)
