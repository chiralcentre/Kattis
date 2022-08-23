from sys import stdin,stdout

def encode_decode(message):
    encrypt,numbers = [],[]
    for c in message:
        encrypt.append(morse[c])
        numbers.append(len(morse[c]))
    encrypted = ''.join(encrypt); start = 0
    for i in range(len(numbers)-1,-1,-1):
        stdout.write(reverse_morse[encrypted[start:start+numbers[i]]])
        start += numbers[i]
    
morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ".": "---.",
    ",": ".-.-",
    "?": "----"
}

reverse_morse = {value: key for key,value in morse.items()}
for line in stdin:
    encode_decode(line.strip())
    stdout.write("\n")
