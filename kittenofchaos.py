from sys import stdin

horizontal = {"b": "d", "d": "b", "q": "p", "p": "q"}
vertical = {"b": "p", "d": "q", "q": "d", "p": "b"}
rotate = {"b": "q", "d": "p", "q": "b", "p": "d"}
s,t = stdin.readline().strip(),stdin.readline().strip()
h,v,r = False,False,False
for letter in t:
    if letter == "h":
        h = not h
    elif letter == "v":
        v = not v
    else:
        r = not r
if h:
    s = "".join(horizontal[char] for char in s[::-1])
if v:
    s = "".join(vertical[char] for char in s)
if r:
    s = "".join(rotate[char] for char in s[::-1])
print(s)
