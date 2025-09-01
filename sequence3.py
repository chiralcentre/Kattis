from sys import stdin

place_anywhere = ["Jd", "Jc"]
remove_anywhere = ["Jh", "Js"]
def solve():
    N = int(stdin.readline())
    in_play = {}
    for _ in range(N):
        # guaranteed spot won't be a Jack
        i,card_played,char,spot = stdin.readline().split()
        freq = in_play.get(spot,0)
        if char == "P":
            if freq == 2 or (card_played != spot and card_played not in place_anywhere):
                return f"INVALID {i}"
            in_play[spot] = freq + 1
        else:
            # only Jacks can remove cards
            if freq == 0 or card_played not in remove_anywhere:
                return f"INVALID {i}"
            in_play[spot] = freq - 1
    return "VALID GAME"
            

if __name__ == "__main__":
    print(solve())
