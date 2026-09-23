from sys import stdin,stdout
import random

def main():
    initialise()
    n = int(stdin.readline())
    snakes,ladders = {},{}
    for _ in range(n):
        s,e = map(int,stdin.readline().split())
        if s > e:
            snakes[s] = e
        elif e > s:
            ladders[s] = e
    p1,p2 = stdin.readline().strip(),stdin.readline().strip()
    winner = play_game(snakes,ladders,p1,p2)
    stdout.write(f"{winner} won the game.\n")

def initialise():
    """Ensure that games play out deterministically by specifying the random seed.

    This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in the autograder.
    """
    random.seed(1337)

# Make use of this function whenever a player rolls a die
def roll_die() -> int:
    return random.randint(1, 6)

def format_roll(p,r,d):
    return f"{p} rolled {r} and is now at square {d}."

def play_game(snakes,ladders,p1,p2):
    steps,players = [0,0],[p1,p2]
    curr,winner = 0,None
    while winner is None:
        r = roll_die()
        d = min(steps[curr] + r,100)
        stdout.write(f"{format_roll(players[curr],r,d)}\n")
        if d in snakes:
            e = snakes[d]
            stdout.write(f"Darn! A snake brought {players[curr]} down to square {e}.\n")
            d = e
        elif d in ladders:
            e = ladders[d]
            stdout.write(f"Splendid! {players[curr]} climbed a ladder up to square {e}.\n")
            d = e
        if d == 100:
            winner = players[curr]
            continue
        steps[curr] = d
        if r != 6:
            curr = (curr + 1) % 2
    return winner

if __name__ == "__main__":
    main()
