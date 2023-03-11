#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef unordered_set<int> usi;

int main() {
    int s; scanf("%d",&s);
    usi points;
    // generate 4 random unique wumpus locations
    while (points.size() < 4) {
        s += s / 13 + 15;
        points.insert(s % 100);
    }
    int moves = 0; int loc;
    while (scanf("%d",&loc) == 1) {
        if (points.find(loc) != points.end()) {
            printf("You hit a wumpus!\n");
            points.erase(loc);
        }
        if (!points.empty()) {
            int lowest = 1e9;
            for (int p: points) lowest = min(lowest, abs(p / 10 - loc / 10) + abs(p % 10 - loc % 10));
            printf("%d\n",lowest);
        }
        moves++;
    }
    printf("Your score is %d moves.\n",moves);
    return 0;
}