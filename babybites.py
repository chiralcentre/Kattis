bites = int(input())
string = input().split()
counter = True
for j in range(len(string)):
    if string[j] != 'mumble' and int(string[j]) != j + 1:
        counter = False
        break

print('makes sense') if counter else print('something is fishy')
