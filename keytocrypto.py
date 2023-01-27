from sys import stdin,stdout

ciphertext,secret = stdin.readline().strip(),stdin.readline().strip()
ans = []
for i in range(min(len(secret),len(ciphertext))):
    ans.append(chr((ord(ciphertext[i]) - ord(secret[i]) + 26) % 26 + ord('A')))
for i in range(len(secret), len(ciphertext)):
    ans.append(chr((ord(ciphertext[i]) - ord(ans[i - len(secret)])) % 26 + ord('A')))
stdout.write("".join(char for char in ans))


