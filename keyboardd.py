from sys import stdin,stdout

s,t = stdin.readline().strip(),stdin.readline().strip()
frequency_table_s,frequency_table_t = {},{}
for char in s:
    frequency_table_s[char] = 1 if char not in frequency_table_s else frequency_table_s[char] + 1
for char in t:
    frequency_table_t[char] = 1 if char not in frequency_table_t else frequency_table_t[char] + 1
for key in frequency_table_s:
    if frequency_table_t[key] == 2*frequency_table_s[key]:
        stdout.write(key)
