#cannot use stdin.readline() since the entire line will be read
print((lambda s: chr(sum(ord(char) for char in s)//len(s)))(input()))
