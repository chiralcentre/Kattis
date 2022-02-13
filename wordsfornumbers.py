from sys import stdin

numbers = {0: 'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
           7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
           13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
           18:'eighteen',19:'nineteen'}
tens = {20:'twenty',30:'thirty',40:'forty',50:'fifty',
        60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

for line in stdin:
    sentence = line.split()
    for i in range(len(sentence)):
        try:
            num = int(sentence[i])
            if 0 <= num <= 19:
                sentence[i] = numbers[num]
            else:
                if num in tens:
                    sentence[i] = tens[num]
                else:
                    ones = num%10
                    closest_ten = num - ones
                    sentence[i] = tens[closest_ten] + '-' + numbers[ones]
            if i == 0:
                sentence[i] = sentence[i].capitalize() #capitalise first word
        except ValueError:
            continue
    print(' '.join(sentence))
