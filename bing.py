from sys import stdin,stdout

prefixes = {}
for i in range(int(stdin.readline())):
    word = stdin.readline().strip()
    stdout.write("0\n") if word not in prefixes else stdout.write(f"{prefixes[word]}\n")
    for j in range(1,len(word)+1): #can be taken to be O(1) since maximum length of word is 32 characters
        part = word[:j]
        prefixes[part] = 1 if part not in prefixes else prefixes[part] + 1
    
