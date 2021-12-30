message = list(input().strip())
#divide
left,right = message[:len(message)//2],message[len(message)//2:]
#rotate
rvl,rvr = sum([ord(char) - 65 for char in left]),sum([ord(char) - 65 for char in right])
left,right = [chr((ord(char)-65+rvl)%26+65) for char in left],[chr((ord(char)-65+rvr)%26+65) for char in right]
#merge
final = [chr((ord(left[i])-65+ord(right[i])-65)%26+65) for i in range(len(message)//2)]
print(''.join(final))
