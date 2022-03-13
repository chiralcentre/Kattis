vowels, counter = {'A','E','I','O','U','a','e','i','o','u'},0
for char in input().strip():
    if char in vowels:
        counter += 1
print(counter)
