from sys import stdin,stdout

puzzle = stdin.readline().strip()
first_letter,repository = puzzle[0],set(puzzle)
for _ in range(int(stdin.readline())):
    word = stdin.readline().strip()
    unique_letters = set(word)
    if len(word) >= 4 and first_letter in unique_letters and len(unique_letters.intersection(puzzle)) == len(unique_letters):
        stdout.write(word+'\n')
