from sys import stdin,stdout

ear,tail = map(float,stdin.readline().split())
ratio = ear / tail
dogs = []
for _ in range(int(stdin.readline())):
    dog_name = stdin.readline().strip()
    lr,hr,le,he = map(float,stdin.readline().split())
    if lr <= ratio <= hr and le <= ear <= he:
        dogs.append(dog_name)
stdout.write("Mutt\n") if not dogs else stdout.write("\n".join(dogs))
