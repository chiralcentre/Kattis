from sys import stdin,stdout

n,code,guess = stdin.readline().split()
n = int(n)
r = 0
code_freq,guess_freq = {},{}
for i in range(n):
    if guess[i] == code[i]:
        r += 1
    else:
        code_freq[code[i]] = 1 if code[i] not in code_freq else code_freq[code[i]] + 1
        guess_freq[guess[i]] = 1 if guess[i] not in guess_freq else guess_freq[guess[i]] + 1
s = sum(min(code_freq[key],guess_freq[key]) for key in code_freq if key in guess_freq)
stdout.write(f"{r} {s}\n")
            
