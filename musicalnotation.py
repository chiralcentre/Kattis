from sys import stdin,stdout

letters_with_dashes = {'F', 'D', 'B', 'g', 'e', 'a'}
all_letters = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

n = int(stdin.readline())
notes = stdin.readline().split()
time = 0
for note in notes:
    if len(note) == 1:
        time += 1
    else:
        time += int(note[1:])
time += len(notes) - 1
mappings = {letter: ["-" if letter in letters_with_dashes else " " for _ in range(time)] for letter in all_letters}
d = 0
for note in notes:
    if len(note) == 1:
        mappings[note][d] = "*"
        d += 2
    else:
        t = int(note[1:])
        for i in range(d,d + t):
            mappings[note[0]][i] = "*"
        d += t + 1
for key,value in mappings.items():
    stdout.write(f"{key}: {''.join(value)}\n")
    
