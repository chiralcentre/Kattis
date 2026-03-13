import re

responses = {
    "A": """Problem A is about Ascii Art
   _     __   __  _   _
  / \\   / /  / / | | | |
 / _ \\  \\ \\ | |  | | | |
/_/ \\_\\ /_/  \\_\\ |_| |_|""",

    "B": """Problem B is about Fortnite
###############
###############
####       /###
####   ########
####       ####
####   ########
####   ########
####   ########
####_~<########
###############""",

    "C": """Problem C is about The Legend of Zelda
     /\\
    /  \\
   /____\\
  /\\    /\\
 /  \\  /  \\
/____\\/____\\"""
}

# use \s+ for flexible spaces
pattern = r"^What\s+is\s+problem\s+([A-C])\s+about\?$"

line = input().strip()
match = re.fullmatch(pattern,line)
if match:
    problem = match.group(1)
    print(responses[problem])  
else:
    print("I am not sure how to answer that.")
