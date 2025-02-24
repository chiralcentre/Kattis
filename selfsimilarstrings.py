from sys import stdin,stdout

# runs in O(n|w|^3), n is number of words, |w| is length of word
for line in stdin:
    w = line.strip()
    ans = 0
    for i in range(1,len(w)):
        t = {}
        for j in range(len(w) - i + 1):
            s = w[j:j + i]
            t[s] = t.get(s,0) + 1
        for key,value in t.items():
            if value < 2:
                break
        else:
            ans = i
    stdout.write(f"{ans}\n")
