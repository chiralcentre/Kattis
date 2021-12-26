found = False
for i in range(5):
    blimp = input().strip()
    for j in range(len(blimp)-2):
        if blimp[j:j+3] == 'FBI':
            found = True
            print(i+1)
            break
if found == False:
    print('HE GOT AWAY!')
