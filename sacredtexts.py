from sys import stdin,stdout

def calculate_rune_value(rune):
    return sum(values[char] for char in rune)

special = {'0':' ','<':',','>':'.'}
values = {chr(i): i - 32 for i in range(33,48)}
alphabet = {chr(i): i - 97 for i in range(97,123)}
sample,letter = stdin.readline().split()
sample_value = calculate_rune_value(sample)
for line in stdin:
    text = line.split()
    for rune in text:
        if len(rune) == 1 and rune[0] in special:
            stdout.write(special[rune[0]])
        else:
            total_value = calculate_rune_value(rune)
            stdout.write(chr((total_value - sample_value + alphabet[letter])%26 + 97))
    stdout.write('\n')
