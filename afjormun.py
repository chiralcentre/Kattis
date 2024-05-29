from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    sentence = stdin.readline().strip()
    stdout.write(sentence[0].upper())
    for i in range(1, len(sentence)):
        stdout.write(sentence[i].lower())
    stdout.write("\n")
