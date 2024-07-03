from sys import stdin

def verify(corpus,words):
    for w in words:
        if w.lower() not in corpus:
            return "Thore has left the chat"
    return "Hi, how do I look today?"

corpus = set(stdin.readline().strip().lower() for _ in range(int(stdin.readline())))
words = stdin.readline().strip().split()
print(verify(corpus,words))
    
