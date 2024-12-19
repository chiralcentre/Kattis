die_mappings = {("       ","   o   ","       "): 1,
                ("     o ","       "," o     "): 2,
                ("     o ","   o   "," o     "): 3,
                (" o   o ","       "," o   o "): 4,
                (" o   o ","   o   "," o   o "): 5,
                (" o   o "," o   o "," o   o "): 6}
                
def parse_dice_input(dice_input):
    freq = {}
    for i in range(5):
        die_string = (dice_input[1][i],dice_input[2][i],dice_input[3][i])
        num = die_mappings[die_string]
        freq[num] = freq.get(num,0) + 1
    return freq

def pair_score(dice_freq):
    res = 0
    for key,value in dice_freq.items():
        if value >= 2:
           res = max(res, key * 2)
    return res

def two_pairs_score(dice_freq):
    at_least_two = []
    for key,value in dice_freq.items():
        if value >= 2:
           at_least_two.append(key)
    return 0 if len(at_least_two) < 2 else sum(at_least_two) * 2

def three_of_a_kind_score(dice_freq):
    for key,value in dice_freq.items():
        if value >= 3:
           return key * 3
    return 0

def four_of_a_kind_score(dice_freq):
    for key,value in dice_freq.items():
        if value >= 4:
           return key * 4
    return 0

def full_house_score(dice_freq):
    if len(dice_freq) != 2:
        return 0
    else:
        v = set(dice_freq.values())
        total = 0
        if 2 in v and 3 in v:
            total = sum(key * value for key,value in dice_freq.items())
        return total

def small_straight_score(dice_freq):
    return 15 if len(dice_freq) == 5 and max(dice_freq.keys()) == 5 else 0

def large_straight_score(dice_freq):
    return 20 if len(dice_freq) == 5 and max(dice_freq.keys()) == 6 and min(dice_freq.keys()) == 2 else 0

def yatzy_score(dice_freq):
    for key,value in dice_freq.items():
        if value == 5:
           return 50
    return 0

def chance_score(dice_freq):
    return sum(key * value for key,value in dice_freq.items())

dice_input = [input().strip() for _ in range(5)]
for i in range(1,5):
    temp = []
    for j in range(5):
        s = 10 * j + 1
        temp.append(dice_input[i][s:s + 7])
    dice_input[i] = temp
    
dice_freq = parse_dice_input(dice_input)
ans = [0 for i in range(15)]
# ones to sixes
for i in range(6):
    ans[i] = dice_freq.get(i + 1,0) * (i + 1)
# pair score
ans[6] = pair_score(dice_freq)
# two pairs score
ans[7] = two_pairs_score(dice_freq)
# three of a kind score
ans[8] = three_of_a_kind_score(dice_freq)
# four of a kind score
ans[9] = four_of_a_kind_score(dice_freq)
# full house score
ans[10] = full_house_score(dice_freq)
# small straight score
ans[11] = small_straight_score(dice_freq)
# large straight score
ans[12] = large_straight_score(dice_freq)
# yatzy score
ans[13] = yatzy_score(dice_freq)
# chance score
ans[14] = chance_score(dice_freq)
print(" ".join(str(num) for num in ans))

