def convert_string_to_mins(time):
    parts = time.split(":")
    return int(parts[0]) * 60 + int(parts[1])

def convert_mins_to_string(mins):
    return f"{mins // 60}:{mins % 60:02d}"

name = input().strip()
time = convert_string_to_mins(input().strip())
day = input().strip()
is_weather_bad = input().strip() == "1"
has_snowed = input().strip() == "1"
is_holiday = input().strip() == "1"
if day == "sat" or day == "sun":
    time *= 2
if is_weather_bad:
    time *= 2
if has_snowed:
    time *= 3
if is_holiday:
    time *= 3
print(convert_mins_to_string(time))
