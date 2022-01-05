smiles = [':)', ';)', ':-)', ';-)']
string = input().strip()
for i in range(len(string)):
    if i + 2 in range(len(string)):
        if string[i:i+3] in smiles:
            print(i)
    if i + 1 in range(len(string)):
        if string[i:i+2] in smiles:
            print(i)
    
