string = input().strip()
length = len(string)
characters = [0,0,0,0]
for char in string:
    if char == '_': #blankspace character
        characters[0] += 1
    elif 97 <= ord(char) <= 122: #lowercase character
        characters[1] += 1
    elif 65 <= ord(char) <= 90: #uppercase character
        characters[2] += 1
    else: #symbols
        characters[3] += 1

for num in characters:
    print(num/length)
