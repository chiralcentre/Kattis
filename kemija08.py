def kemija(string):
    vowels = ['a','e','i','o','u']
    s2 = ''
    while string:
        char = string[0]
        if char not in vowels:
            s2 += char
            string = string[1:]
        else:
            s2 += char
            string = string[3:]
    return s2

sentence = input()
print(kemija(sentence))
    
            
        
