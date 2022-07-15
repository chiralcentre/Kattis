from sys import stdin,stdout

compoundwords = set()
words = []
for line in stdin:
    w = line.split()
    words.extend(w)
#O(n^2) where n is number of words
for w1 in words:
    for w2 in words:
        if w1 != w2:
            compoundwords.add(w1+w2)
            compoundwords.add(w2+w1)
#O(n^2 log n^2) where n is number of words
for word in sorted(compoundwords):
    stdout.write(word+"\n")
