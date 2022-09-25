from sys import stdin,stdout

soundex = [0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
for line in stdin:
    word = line.strip()
    code = []
    for i in range(len(word)):
        index = ord(word[i]) - 65
        if soundex[index] != 0 and (i == 0 or soundex[index] != soundex[ord(word[i-1])-65]):
            code.append(str(soundex[index]))
    stdout.write(''.join(num for num in code)+'\n')
