def playfair(digraph,table):
    a,b = digraph[0],digraph[1]
    x1,y1 = table[a]
    x2,y2 = table[b]
    #If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively
    # same row = same x coordinates
    if x1 == x2:
        for k,value in table.items():
            if value == (x1,(y1+1)%5):
                a = k
            elif value == (x2,(y2+1)%5):
                b = k
        return a+b
                        
    #If the letters appear on the same column of your table, replace them with the letters immediately below respectively
    elif y1 == y2:
        for k,value in table.items():
            if value == ((x1+1)%5,y1):
                a = k
            elif value == ((x2+1)%5,y2):
                b = k
        return a+b
    #If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other group of corners of the rectangle defined by the original group.\   
    #The order is important – the first letter of the encrypted group is the one that lies on the same row as the first letter of the plaintext group.
    else:
        for k,value in table.items():
            if value == (x1,y2):
                a = k
            elif value == (x2,y1):
                b = k
        return a+b
    
alphabet = [chr(i) for i in range(65,91) if i!= 81] #'A' to 'Z' except 'Q'

keyphrase = ''.join(input().split()).upper()
lst,key = [],{}

for char in keyphrase:
    if char not in lst:
        lst.append(char)
        alphabet.remove(char)
        
lst2 = lst + alphabet
# encryption key is in coordinate form; x coordinate is row number and y coordinate is column number
for i in range(25):
    key[lst2[i]] = (i//5,i%5) 

message = ''.join(input().split()).upper()
encrypted = []
        
while message:
    #If both letters are the same (or only one letter is left), add an ‘X’ after the first letter.
    #Encrypt the new group and continue (note that this changes all the remaining digraphs).
    if len(message) == 1: 
        encrypted.append(playfair(message[0] + 'X',key))
        message = ''
    else:
        group = message[0:2]
        message = message[2:]
        if group[0] == group[1]:
            message = group[0] + 'X' + group[1] +  message
        else:
            encrypted.append(playfair(group,key))
            
print(''.join(encrypted))
