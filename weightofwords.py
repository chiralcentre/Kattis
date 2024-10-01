l,w = map(int,input().split())
if l * 26 < w or l > w:
    print("impossible")
else:
    average,rem = w // l,w % l
    for i in range(rem):
        print(chr(97 + average),end="")
    for i in range(l - rem):
        print(chr(96 + average),end="")

