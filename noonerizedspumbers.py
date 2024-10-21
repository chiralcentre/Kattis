# complete search
def solve():
    expr = input().split()
    x,op,y,z = expr[0],expr[1],expr[2],expr[4]
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            tx = y[:j] + x[i:]
            ty = x[:i] + y[j:]
            res = eval(f"{tx} {op} {ty}")
            if res == int(z):
                return f"{tx} {op} {ty} = {z}"
    for i in range(1,len(x)):
        for j in range(1,len(z)):
            tx = z[:j] + x[i:]
            tz = x[:i] + z[j:]
            res = eval(f"{tx} {op} {y}")
            if res == int(tz):
                return f"{tx} {op} {y} = {tz}"
    for i in range(1,len(y)):
        for j in range(1,len(z)):
            ty = z[:j] + y[i:]
            tz = y[:i] + z[j:]
            res = eval(f"{x} {op} {ty}")
            if res == int(tz):
                return f"{x} {op} {ty} = {tz}"


print(solve())
