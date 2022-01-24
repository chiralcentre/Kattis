alphabet = {chr(num) for num in range(97,123)}
for _ in range(int(input())):
    phrase = input().strip().lower()
    print(f"missing {''.join(list(letter for letter in sorted(list(alphabet-set(phrase)))))}") if len(alphabet-set(phrase)) else print("pangram") 
