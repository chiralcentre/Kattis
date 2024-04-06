def solve(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1] or (i + 2 < len(text) and text[i] == text[i + 2]):
            return "Palindrome"
    return "Anti-palindrome"

def remove_spaces(text):
    return "".join(char for char in text if char != " ")

print(solve(remove_spaces(input().strip().lower())))
