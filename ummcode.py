from sys import stdin,stdout

allowed = {chr(c) for c in range(32,127)}
for i in range(48,58): #remove all digits
    allowed.remove(chr(i))
for i in range(65,91): #remove all upper case letters
    allowed.remove(chr(i))
for i in range(97,123): #remove all lower case characters, add back u and m later
    allowed.remove(chr(i))
allowed.add("u")
allowed.add("m")

def ummword(word):
    for i in range(len(w)):
        if w[i] not in allowed:
            return False
    return True

words = stdin.readline().split()
message = []
for w in words:
    if ummword(w):
        for i in range(len(w)):
            if w[i] == "u":
                message.append(1)
            elif w[i] == "m":
                message.append(0)
                
for i in range(0,len(message),7):
    stdout.write(chr(sum(pow(2,6 - j) for j in range(7) if message[i + j] == 1)))
