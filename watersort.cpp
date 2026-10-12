#include <bits/stdc++.h>
using namespace std;

// Vials are vectors of colours (0 = 'a'), bottom to top. {} is an empty vial.
const int CAPACITY = 4;

uint64_t mix(uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

// Each vial gets an exact code (base 17, colour + 1 per layer), then a random-looking hash.
uint64_t vialHash(const vector<int>& vial) {
    uint64_t code = 0;
    for (int colour : vial) code = code * 17 + (colour + 1);
    return mix(code);
}

// Summing makes the key independent of vial order, so boards never need sorting.
uint64_t boardHash(const vector<vector<int>>& board) {
    uint64_t key = 0;
    for (const vector<int>& vial : board) key += vialHash(vial);
    return key;
}

int topColour(const vector<int>& vial) {
    return vial.back();
}

int topRunLength(const vector<int>& vial) {
    int run = 1;
    int i = (int)vial.size() - 2;
    while (i >= 0 && vial[i] == topColour(vial)) {
        run++;
        i--;
    }
    return run;
}

bool isSingleColour(const vector<int>& vial) {
    return topRunLength(vial) == (int)vial.size();
}

bool isFinished(const vector<int>& vial) {
    if (vial.empty()) return true;
    return (int)vial.size() == CAPACITY && isSingleColour(vial);
}

bool isSolved(const vector<vector<int>>& board) {
    for (const vector<int>& vial : board)
        if (!isFinished(vial)) return false;
    return true;
}

struct State {
    vector<vector<int>> board;
    uint64_t key;
};

struct Move {
    State result;
    int cost;
};

vector<Move> possibleMoves(const State& state) {
    const vector<vector<int>>& board = state.board;
    vector<Move> moves;
    bool triedEmptyTarget = false;

    for (int to = 0; to < (int)board.size(); to++) {
        const vector<int>& target = board[to];
        if ((int)target.size() == CAPACITY) continue;

        // Empty vials are interchangeable: only try one.
        if (target.empty()) {
            if (triedEmptyTarget) continue;
            triedEmptyTarget = true;
        }

        for (int from = 0; from < (int)board.size(); from++) {
            if (from == to) continue;
            const vector<int>& source = board[from];
            if (source.empty()) continue;

            int colour = topColour(source);
            if (!target.empty() && topColour(target) != colour) continue;

            // Moving a single-colour vial into an empty one never helps.
            if (target.empty() && isSingleColour(source)) continue;

            int freeSpace = CAPACITY - (int)target.size();
            int amount = min(topRunLength(source), freeSpace);

            State next = state;
            next.key -= vialHash(source) + vialHash(target);
            next.board[from].resize(source.size() - amount);
            next.board[to].insert(next.board[to].end(), amount, colour);
            next.key += vialHash(next.board[from]) + vialHash(next.board[to]);

            moves.push_back({move(next), amount});
        }
    }
    return moves;
}

// Dial's algorithm: costs are 1..3, so 4 circular buckets suffice.
int shortestSolution(const vector<vector<int>>& start) {
    const int BUCKETS = 4;
    vector<vector<State>> bucket(BUCKETS);
    unordered_map<uint64_t, int> bestDistance;
    bestDistance.reserve(1 << 20);

    State first = {start, boardHash(start)};
    bestDistance[first.key] = 0;
    bucket[0].push_back(first);
    int statesWaiting = 1;

    for (int distance = 0; statesWaiting > 0; distance++) {
        vector<State>& current = bucket[distance % BUCKETS];

        while (!current.empty()) {
            State state = move(current.back());
            current.pop_back();
            statesWaiting--;

            // Skip outdated entries.
            if (bestDistance[state.key] != distance) continue;

            if (isSolved(state.board)) return distance;

            for (Move& m : possibleMoves(state)) {
                int newDistance = distance + m.cost;
                auto found = bestDistance.find(m.result.key);

                if (found == bestDistance.end() || newDistance < found->second) {
                    bestDistance[m.result.key] = newDistance;
                    bucket[newDistance % BUCKETS].push_back(move(m.result));
                    statesWaiting++;
                }
            }
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;

    // Input lines are layers, top first; column i is vial i.
    vector<vector<char>> rows(CAPACITY, vector<char>(n));
    for (int r = 0; r < CAPACITY; r++)
        for (int i = 0; i < n; i++)
            cin >> rows[r][i];

    vector<vector<int>> start(n + 2);
    for (int i = 0; i < n; i++)
        for (int r = CAPACITY - 1; r >= 0; r--)
            start[i].push_back(rows[r][i] - 'a');

    cout << shortestSolution(start) << "\n";
    return 0;
}