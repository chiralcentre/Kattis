from sys import stdout

vowels = {"a", "e", "i","o","u"}
s = input().strip()
for char in s:
    if char in vowels:
        stdout.write(char)
    elif char == "-":
        stdout.write("\n")
    elif char.isnumeric():
        stdout.write(bin(int(char))[2:])
    else:
        stdout.write("beepbloop")
