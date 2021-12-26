def texture(s1):
    dict1,counts,count = {},set(),0
    for char in s1:
        if char == '*':
            if char in dict1.keys():
                counts.add(count)
                count = 0
            else:
                dict1['*'] = 1
        elif char == '.':
            count += 1
    return 'EVEN' if len(counts) == 1 or len(counts) == 0 else 'NOT EVEN'

counter = 1
while True:
    string = input().strip()
    if string == 'END':
        break
    print(f'{counter} {texture(string)}')
    counter += 1
