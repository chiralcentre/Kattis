alphabet = 'abcdefghijklmnopqrstuvwxyz'

inpt = input().strip()

counter = 26

for i in range(len(inpt)):
    for j in range(i,len(inpt)):
        if inpt[i:j+1] in alphabet:
            num = 26 - len(inpt[i:j+1])
            if num < counter:
                counter = num
print(counter)
            

