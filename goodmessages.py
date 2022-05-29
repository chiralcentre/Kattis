from sys import stdin,stdout

O = int(stdin.readline())
happy_steps,unhappy_steps = 0,0
message = stdin.readline().strip()
normalised_message = [ord(char)-97 for char in message] #replace character with normalised ascii code, with 'a' having value of 0
vowels = {0,4,8,14,20,24} #'a','e','i','o','u','y'
for i in range(int(stdin.readline())):
    v = 0
    for j in range(len(normalised_message)):
        normalised_message[j] = (normalised_message[j]+O)%26
        if normalised_message[j] in vowels:
            v += 1
    #2*v >= c -> 2*v >= len(normalised_message) - v -> 3*v >= len(normalised_message)
    if 3*v >= len(normalised_message):
        unhappy_steps += 1
    else:
        happy_steps += 1
        
stdout.write("Boris\n") if happy_steps > unhappy_steps else stdout.write("Colleague\n")
