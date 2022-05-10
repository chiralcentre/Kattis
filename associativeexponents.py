from math import log
a,b,c = map(int,input().split())
#b*c == b**c -> log c = (c-1)log b
print("What an excellent example!") if a == 1 or log(c) == (c-1)*log(b) else print("Oh look, a squirrel!")
