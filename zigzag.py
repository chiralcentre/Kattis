from sys import stdin,stdout

k = int(stdin.readline())
#find minimum number of differences required
#25 is the maximum consecutive difference ("a" and "z")
d = k // 25 + 1 if k % 25 else k // 25
if d == 1:
    stdout.write("a")
    stdout.write(chr(97 + k))
elif d == 2:
    m = k // 2 + 1 if k % 2 else k // 2
    stdout.write("a")
    stdout.write(chr(97 + m))
    stdout.write("b") if k % 2 else stdout.write("a")
else:
    # assume last d - 2 differences are 25
    R = (d - 2) * 25; L = k - R
    if L % 2:
        L += 1;
        R -= 1
    stdout.write("a")
    stdout.write(chr(97 + L // 2))
    stdout.write("a") 
    prev = "a"
    for i in range(d - 2):
        if R >= 25:
            prev = "z" if prev == "a" else "a"
            R -= 25
            stdout.write(prev)
        else:
            prev = chr(ord("z") - R) if prev == "z" else chr(ord("a") + R)
            stdout.write(prev)
    

    
