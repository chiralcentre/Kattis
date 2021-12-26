string = input().strip()

counter,name = 0,'PER'
for i in range(0,len(string),3):
    snippet = string[i:i+3]
    for j in range(3):
        if snippet[j] != name[j]:
            counter += 1
        
print(counter)
    
