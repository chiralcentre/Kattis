signs = {"+", "-"}

def check_valid_coordinates(coords):
    # look for * marker
    first_split = coords.split("*")
    # check if there is exactly one * marker
    if len(first_split) != 2:
        return False,None
    first_part,second = first_split
    # check that there is a sign
    if not first_part or first_part[0] not in signs:
        return False,None
    # check if number of digits is correct, with no leading zeroes
    if first_part[1] == "0" and len(first_part) != 2:
        return False,None
    # check if integer conversion is possible
    try:
        degrees = int(first_part)
    except Exception:
        return False,None
    # check if degrees is within range
    if not -360 <= degrees <= 360:
        return False,None
    
    # look for ' marker
    second_split = second.split("'")
    # check if there is exactly one ' marker
    if len(second_split) != 2:
        return False,None
    second_part,third = second_split
    # check if number of digits is correct
    if len(second_part) != 2:
        return False,None
    # check if integer conversion is possible
    try:
        minutes = int(second_part)
    except Exception:
        return False,None
    # check if minutes is within range
    if not 0 <= minutes <= 59:
        return False,None
    
    # look for " marker
    third_split = third.split('"')
    # check if there is exactly one " marker
    if len(third_split) != 2:
        return False,None
    third_part = third_split[0]
    # check if number of digits is correct
    if len(third_part) != 2:
        return False,None
    # check if integer conversion is possible
    try:
        seconds = int(third_part)
    except Exception:
        return False,None
    # check if seconds is within range
    if not 0 <= seconds <= 59:
        return False,None
    return True,(degrees,minutes,seconds)

def solve():
    string = input().strip()
    parts = string.split(" ")
    # should have both longitude and latitude
    if len(parts) != 2:
        return "False"
    is_lat_valid,lat_res = check_valid_coordinates(parts[0])
    is_long_valid,long_res = check_valid_coordinates(parts[1])
    if not (is_lat_valid and is_long_valid):
        return "False"
    bd,bm,bs = lat_res
    if not -90 <= bd <= 90 or ((bd == 90 or bd == -90) and (bm > 0 or bs > 0)):
        return "False"
    ld,lm,ls = long_res
    if not 0 <= ld <= 360 or ((ld == 360 or ld == 0) and (lm > 0 or ls > 0)):
        return "False"
    return "True"

print(solve())
