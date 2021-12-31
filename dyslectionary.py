def d_sort(longest,words):
    for word in sorted(words,key = lambda w: w[::-1]):
        print(' '*(longest-len(word))+word)
        
length_max,dyslectionary = 0,[]
while True:
    try:
        word = input()
        #print(word)
        if not word:
            d_sort(length_max,dyslectionary)
            print() # a new line
            length_max,dyslectionary = 0,[] #restart
        else:
            length_max = max(length_max,len(word))
            dyslectionary.append(word)
    except EOFError: #end of file
        d_sort(length_max,dyslectionary)
        break

        
     
