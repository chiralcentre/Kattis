from sys import stdin,stdout

def find_replacement(total):
    for key,value in lengths.items():
        if total + value == key:
            return words[key]
        
words = {1:"one",2:"two",3:"three",4:"four",5:"five",
         6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
         11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",
         15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
         19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",
         60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"onehundred",
         200:"twohundred",300:"threehundred",400:"fourhundred",500:"fivehundred",
         600:"sixhundred",700:"sevenhundred",800:"eighthundred",900:"ninehundred"}
#lengths[a] contains the length of the string representing the number a
lengths = {}
for i in range(21,100):
    if i%10: #not a multiple of 10
        tens_digit = i//10
        words[i] = words[tens_digit*10] + words[i-tens_digit*10]
for j in range(101,1000):
    if j%100: #not a multiple of 100
        hundreds_digit = j//100
        words[j] = words[hundreds_digit*100] + words[j-hundreds_digit*100]
for key in words:
    lengths[key] = len(words[key])

index,sentence,total = -1,[],0
for i in range(int(stdin.readline())):
    w = stdin.readline().strip()
    if w != "$":
        total += len(w)
    else:
        index = i
    sentence.append(w)
sentence[index] = find_replacement(total)
stdout.write(" ".join(sentence))


