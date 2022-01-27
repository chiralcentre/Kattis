from collections import defaultdict

users,keywords = defaultdict(set),defaultdict(lambda:0)
for _ in range(int(input())):
    name, *message = input().split()
    for word in message:
        users[name].add(word)
        keywords[word] += 1

common_words = set.intersection(*users.values())
# sort by value then alphabetical order, negative sign is used to sort in descending order for words
print('\n'.join(sorted(common_words,key = lambda x: (-keywords[x],x)))) if common_words else print('ALL CLEAR')
        
