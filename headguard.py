from sys import stdin,stdout

for line in stdin:
    prev,counter = line[0],0
    for char in line.strip():
        if char == prev:
            counter += 1
        else:
            stdout.write(f"{counter}{prev}")
            prev = char
            counter = 1      
    stdout.write(f"{counter}{prev}\n")
