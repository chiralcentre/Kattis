#include <bits/stdc++.h>
#include <string>

using namespace std;

typedef pair<int,int> ii;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef unordered_map<char,ii> cii;
typedef unordered_map<string,ii> sii;

sii movements = {{"up", make_pair(-1,0)}, {"down", make_pair(1,0)},
                {"left", make_pair(0,-1)},{"right", make_pair(0,1)}};

// trim from end (in place)
static inline void rtrim(string &s) {
    s.erase(find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
        return !isspace(ch);}).base(), s.end());
}

int horizontalBound(vvc &board, int step) {
    int s = (step == 1 ? 0 : board.size() - 1);
    int e = (step == 1 ? board.size() - 1: 0);
    for (int j = s; (step == 1 ? j <= e : j >= e); j += step) {
        for (int i = 0; i <= board.size() - 1; i++) {
            if (board[i][j] != ' ') return j;
        }
    }
}

int verticalBound(vvc &board, int step) {
    int s = (step == 1 ? 0 : board.size() - 1);
    int e = (step == 1 ? board.size() - 1: 0);
    for (int i = s; (step == 1 ? i <= e : i >= e); i += step) {
        for (int j = 0; j <= board.size() - 1; j++) {
            if (board[i][j] != ' ') return i;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (true) {
        int N; cin >> N;
        if (N == -1) break;
        cii coordinates; vvc board(5 + 2 * N, vc (5 + 2 * N, ' '));
        // fill in the 25 letter tiles
        for (int i = N; i <= N + 4; i++) {
            for (int j = N; j <= N + 4; j++) {
                board[i][j] = 65 + (i - N) * 5 + j - N;
                coordinates[board[i][j]] = make_pair(i,j);
            }
        }
        for (int k = 0; k < N; k++) {
            char prev; string d; 
            cin >> prev >> d;
            ii p1 = coordinates[prev], p2 = movements[d];
            int x = p1.first, y = p1.second;
            int i = p2.first, j = p2.second;
            board[x][y] = ' ';
            char next = board[x + i][y + j];
            if (next == ' ') {
                board[x + i][y + j] = prev;
                coordinates[prev] = make_pair(x + i, y + j);
            }
            while (next != ' ') {
                next = board[x + i][y + j];
                board[x + i][y + j] = prev;
                coordinates[prev] = make_pair(x + i, y + j);
                x += i; y += j;
                prev = next;
            }
        }
        int left = horizontalBound(board,1), right = horizontalBound(board,-1);
        int top = verticalBound(board,1), bottom = verticalBound(board,-1);
        for (int i = top; i <= bottom; i++) {
            string s = "";
            for (int j = left; j <= right; j++) s += board[i][j];
            rtrim(s);
            cout << s << "\n";
        }
        cout << "\n";
    }
    return 0;
}