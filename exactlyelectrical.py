a,b = map(int,input().split())
c,d = map(int,input().split())
t = int(input())
manhattan_d = abs(a-c) + abs(b-d)
#print yes if difference between manhattan distance and electrical charge is a multiple of 2, as this means back and forth trips can be made
print('N') if manhattan_d > t else print('Y') if not (t-manhattan_d)%2 else print('N')

'''
# longer version of code
if manhattan_d > t:
    print('N')
else:
    print('Y') if not (t-manhattan_d)%2 else print('N') 
'''
