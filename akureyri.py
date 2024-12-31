from sys import stdin,stdout

places = {}
for _ in range(int(stdin.readline())):
    stdin.readline()
    location = stdin.readline().strip()
    places[location] = places.get(location,0) + 1
for location,count in places.items():
    stdout.write(f"{location} {count}\n")
