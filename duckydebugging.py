end = False
while not end:
    line = input().strip()
    if line[-1] == "?":
        print("Quack!")
    elif line[-1] == ".":
        print("*Nod*")
    elif line[-1] == "!":
        end = True
        
