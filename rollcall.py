from sys import stdin,stdout

firstName,lastName,people = {},{},[]
for line in stdin:
    F,L = line.split()
    firstName[F] = 1 if F not in firstName else firstName[F] + 1
    lastName[L] = 1 if L not in lastName else lastName[L] + 1
    people.append((F,L))
people.sort(key = lambda x: (x[1],x[0])) #sort by last name, then first name if there is a tie
for F,L in people:
    stdout.write(f"{F} {L}\n") if firstName[F] > 1 else stdout.write(f"{F}\n")
