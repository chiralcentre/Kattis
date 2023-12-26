from sys import stdin,stdout

def contains_letter(alphabet,w):
    for char in w:
        if char in alphabet:
            return True
    return False

alphabet = set(stdin.readline().strip())
words = stdin.readline().strip().split()
for i in range(len(words)):
    stdout.write("*" * len(words[i])) if contains_letter(alphabet,words[i]) else stdout.write(words[i])
    if i < len(words) - 1:
        stdout.write(" ")
