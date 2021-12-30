def unique(s,dict1):
    for char in s:
        if len(dict1[char]) > 1:
            return False
    return True

n = int(input())
s = input().split()
dutch_dict = {}
for i in range(int(input())):
    d,e,c = input().split()
    if d not in dutch_dict:
        dutch_dict[d] = [(e,'C')] if c == 'correct' else [(e,'I')]
    else:
        dutch_dict[d] += [(e,'C')] if c == 'correct' else [(e,'I')]

if unique(s,dutch_dict):
    correct,translation = True,[]
    for char in s:
        e,c = dutch_dict[char][0]
        translation.append(e)
        if c == 'I':
            correct = False
    print(' '.join(translation))
    print('correct') if correct else print('incorrect')
else:
    lst,total,correct = [],1,1
    for char in s:
        C,I = 0,0
        for pair in dutch_dict[char]:
            if pair[1] == 'C':
                C += 1
        lst.append(C)
        total *= len(dutch_dict[char])
    for num in lst:
        correct *= num
    print(f'{correct} correct')
    print(f'{total - correct} incorrect') #incorrect cases are complement of correct cases
        
