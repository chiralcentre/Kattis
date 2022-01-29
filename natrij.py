h1,m1,s1 = map(int,input().split(":"))
h2,m2,s2 = map(int,input().split(":"))

seconds = (h2-h1)*3600 + (m2-m1)*60 + s2-s1 if h1 < h2 else (h2+24 - h1)*3600 + (m2-m1)*60 + s2-s1

h3,m3,s3 = seconds//3600, (seconds%3600)//60,seconds%60
print(f"0{h3}:",end="") if h3 < 10 else print(f"{h3}:",end="")
print(f"0{m3}:",end="") if m3 < 10 else print(f"{m3}:",end="")
print(f"0{s3}",end="") if s3 < 10 else print(f"{s3}",end="")
