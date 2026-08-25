vowels = {"a","e","i","o","u"}

s = input().strip()
end = None
for i in range(len(s) - 1, -1, -1):
    if s[i] in vowels:
        end = i
        break
print(s[:i + 1] + "ntry")
