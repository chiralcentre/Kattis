N = int(input())
original,modified = list(input().strip()),list(input().strip())

for i in range(N):
    for j in range(len(original)):
        original[j] = '1' if original[j] == '0' else '0'

print('Deletion succeeded') if original == modified else print('Deletion failed')
