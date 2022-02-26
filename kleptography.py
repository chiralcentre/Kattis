from sys import stdin,stdout
from collections import deque
n,m = map(int,stdin.readline().split())
last_letters,ciphertext = stdin.readline().strip(),stdin.readline().strip()
plaintext = deque([])
for char in last_letters:
    plaintext.append(char)
counter = 1
for i in range(m-1,n-1,-1):
    plaintext.appendleft(chr((ord(ciphertext[-counter])+26-ord(plaintext[n-1]))%26+97))
    counter += 1
print(''.join(plaintext))
    
