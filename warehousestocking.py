from sys import stdin,stdout

items_locations = {}
locations_items = {}
N = int(stdin.readline())
for _ in range(N):
    instruction = stdin.readline().split()
    if instruction[0] == "PUT":
        item,location = instruction[1],instruction[2]
        locations_items[location] = item
        if item in items_locations:
            items_locations[item].add(location)
        else:
            items_locations[item] = {location}
    elif instruction[0] == "TAKE":
        location = instruction[1]
        item = locations_items.pop(location)
        items_locations[item].remove(location)
    else: # taken to be O(1) time since there are only at most 10 copies of each item
        item = instruction[1]
        if item not in items_locations or len(items_locations[item]) == 0:
            stdout.write("NOT FOUND\n")
        else:
            stdout.write(" ".join(sorted(items_locations[item])))
            stdout.write("\n")
