addends = int(input())
counter,total = 0,0
while counter < addends:
    inpt = input().strip()
    number = int(inpt[:-1])
    power = int(inpt[-1])
    total += number**power
    counter += 1
print(total)
