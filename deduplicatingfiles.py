from sys import stdin,stdout

def hashing(string):
    ans = ord(string[0])
    for i in range(1,len(string)):
        ans ^= ord(string[i])
    return ans

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    files,hashes = {},{}
    for i in range(n):
        filename = stdin.readline().strip('\n')
        files[filename] = 1 if filename not in files else files[filename] + 1
        h = hashing(filename)
        if h not in hashes:
            hashes[h] = {filename}
        else:
            hashes[h].add(filename)
    collisions = 0
    for h,s in hashes.items():
        unique = list(s)
        for i in range(len(unique)):
            for j in range(i+1,len(unique)):
                collisions += files[unique[i]]*files[unique[j]]
    stdout.write(f"{len(files)} {collisions}\n")
   
    
