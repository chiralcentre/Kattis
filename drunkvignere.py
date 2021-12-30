m1,key = input().strip(),input().strip()
final = [chr((ord(m1[i])+ord(key[i])-130)%26+65) if i%2 else chr((ord(m1[i])-ord(key[i])-130)%26+65) for i in range(len(m1))]
print(''.join(final))   
