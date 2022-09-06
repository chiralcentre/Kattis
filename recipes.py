from sys import stdin,stdout

for j in range(int(stdin.readline())):
    R,P,D = map(int,stdin.readline().split())
    SCALE,ingredients = D/P,[]
    main,main_w = "",-1
    for i in range(R):
        ingredient,w,p = stdin.readline().split()
        w,p = float(w),float(p)
        if p == 100.0:
            main,main_w = ingredient,w*SCALE
        ingredients.append((ingredient,p))
    stdout.write(f"Recipe # {j+1}\n")
    for ig,p in ingredients:
        stdout.write(f"{ig} {main_w*p/100}\n")
    stdout.write("-" * 40 + "\n")
