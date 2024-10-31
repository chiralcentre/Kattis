from sys import stdin,stdout

qwerty = [
    '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'
]

dvorak = [
    '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']',
    "'", ',', '.', 'p', 'y', 'f', 'g', 'c', 'r', 'l', '/', '=',
    'a', 'o', 'e', 'u', 'i', 'd', 'h', 't', 'n', 's', '-',
    ';', 'q', 'j', 'k', 'x', 'b', 'm', 'w', 'v', 'z'
]

bjarki = [
    '0', '2', '4', '8', '6', '1', '3', '5', '7', '9', '=', '-', '/',
    'b', 'j', 'a', 'r', 'k', 'i', 'g', 'u', 's', 't', '.', ',',
    'l', 'o', 'e', 'm', 'p', 'd', 'c', 'n', 'v', 'q', ';',
    '[', ']', 'y', 'z', 'h', 'w', 'f', 'x', "'", '~'
]

mappings = {}
mappings["qwertydvorak"] = {qwerty[i]: dvorak[i] for i in range(len(qwerty))}
mappings["dvorakqwerty"] = {dvorak[i]: qwerty[i] for i in range(len(qwerty))}
mappings["dvorakbjarki"] = {dvorak[i]: bjarki[i] for i in range(len(qwerty))}
mappings["bjarkidvorak"] = {bjarki[i]: dvorak[i] for i in range(len(qwerty))}
mappings["qwertybjarki"] = {qwerty[i]: bjarki[i] for i in range(len(qwerty))}
mappings["bjarkiqwerty"] = {bjarki[i]: qwerty[i] for i in range(len(qwerty))}

t1,e,t2 = stdin.readline().split()
line = stdin.readline().strip()
if t1 == t2:
    stdout.write(line)
else:
    d = mappings[t1 + t2]
    stdout.write("".join(d.get(char," ") for char in line))
    
    
