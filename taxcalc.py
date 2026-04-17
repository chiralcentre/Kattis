from sys import stdin,setrecursionlimit

setrecursionlimit(1000000)
def evaluate(tokens, i=0):
    token = tokens[i]
    if token == '(':
        op = tokens[i + 1]
        i += 2
        values = []
        while tokens[i] != ')':
            val, i = evaluate(tokens, i)
            values.append(val)
        i += 1  # skip ')'
        if op == '+':
            return sum(values), i
        elif op == '-':
            return values[0] - values[1],i
        elif op == '/':
            return values[0] // values[1], i
        else:
            raise ValueError(f"Unknown operator {op}")
    else:
        return int(token), i + 1

taxcalc = stdin.readline().strip()
print(evaluate(taxcalc.split())[0])
