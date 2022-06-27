from sys import stdin,stdout

def count_double_vowels(string,vowelpairs):
    counter = 0
    for i in range(len(string)-1):
        if string[i] + string[i+1] in vowelpairs:
            counter += 1
    return counter

vowelpairs = {'aa','ee','ii','oo','uu','yy'}
while True:
    N = int(stdin.readline())
    if N == 0:
        break
    highest,favourite = -1,''
    for i in range(N):
        word = stdin.readline().strip()
        double_vowel_count = count_double_vowels(word,vowelpairs)
        if double_vowel_count > highest: #unique correct answer, no need to check for equality
            highest = double_vowel_count
            favourite = word
    stdout.write(favourite+'\n')
