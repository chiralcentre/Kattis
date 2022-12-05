# (A - C) x < (D - B) -> f(x) < g(x) -> h(x) = g(x)
# (A - C) x > (D - B) -> f(x) > g(x) -> h(x) = f(x)
#f(x) attains minimum at -A/2 and g(x) attains minimum at -C/2
def f(A,B,x):
    return x**2 + A*x + B

A,B,C,D = map(int,input().split())
if A - C == 0:
    x = -A/2
    m = f(A,max(B,D),x)
    print(f"{x} {m}")
else:
    E = (D - B)/(A - C)
    # (A - C) x < (D - B) -> x < (D - B)/(A - C) -> f(x) < g(x) -> h(x) = g(x)
    # (A - C) x > (D - B) -> x > (D - B)/(A - C) -> f(x) > g(x) -> h(x) = f(x)
    if A - C > 0:
        #find local minima for g(x) in x < E
        x1,m1 = 0,0
        if -C/2 < E:
            x1,m1 = -C/2,f(C,D,-C/2)
        else:
            x1,m1 = E,f(C,D,E)
        #find local minima for f(x) in x > E
        x2,m2 = 0,0
        if -A/2 > E:
            x2,m2 = -A/2,f(A,B,-A/2)
        else:
            x2,m2 = E,f(A,B,E)
    # (A - C) x < (D - B) -> x > (D - B)/(A - C) -> f(x) < g(x) -> h(x) = g(x)
    # (A - C) x > (D - B) -> x < (D - B)/(A - C) -> f(x) > g(x) -> h(x) = f(x)
    else:
        #find local minima for g(x) in x < E
        x1,m1 = 0,0
        if -C/2 > E:
            x1,m1 = -C/2,f(C,D,-C/2)
        else:
            x1,m1 = E,f(C,D,E)
        #find local minima for f(x) in x > E
        x2,m2 = 0,0
        if -A/2 < E:
            x2,m2 = -A/2,f(A,B,-A/2)
        else:
            x2,m2 = E,f(A,B,E)
    print(f"{x1} {m1}") if m1 < m2 else print(f"{x2} {m2}")
    


