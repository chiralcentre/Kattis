from sys import stdin,stdout

# code runs in O(n^2), where n is length of string
def palindromicSubstring(string):
    n = len(string)
    result = set()
    # check for odd length palindromes
    for i in range(n):
        left = i
        right = i
        while left >= 0 and right < n and string[left] == string[right]:
            if right != left:
                result.add(string[left:right+1])
            left -= 1
            right += 1
    # check for even length palindromes
    for i in range(n - 1):
        left = i
        right = i + 1
        while left >= 0 and right < n and string[left] == string[right]:
            result.add(string[left:right+1])
            left -= 1
            right += 1
    return sorted(result)

for line in stdin:
    line = line.strip()
    for s in palindromicSubstring(line):
        stdout.write(f"{s}\n")
    stdout.write("\n")
