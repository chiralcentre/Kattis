mappings = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04",
            "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08",
            "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"
            }

d,m,m2,y = input().split()
m2 = m2[1:]
print(f"20{y}-{mappings[m2]}-{d}")
