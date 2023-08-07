#include <bits/stdc++.h>

using namespace std;

const int S = 26;
bool one[S];
bool two[S][S];
int three[S][S][S];
vector<string> words;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,M; cin >> N >> M;
    memset(three,-1,sizeof(three));
    for (int i = 0; i < N; ++i) {
        memset(one,0,sizeof(one)); // set everything to false
        memset(two,0,sizeof(two)); // set everything to false
        string word; cin >> word;
        for (int j = 0; j < word.length(); ++j) {
            for (int k = 0; k < S; ++k) {
                for (int l = 0; l < S; ++l)
                //check if three[k][l][word[j] - 'a'] is performed to ensure that a previous word containing the subsequence has not been found
                    if (two[k][l] && three[k][l][word[j]-'a'] == -1) three[k][l][word[j]-'a'] = i; // subsequence of three has been seen
                    two[k][word[j]-'a'] |= one[k]; // records that subsequence of two with first letter being the kth letter and secord letter at position j has been seen
            }
            one[word[j]-'a'] = true; // records that letter at position j has been seen
        }
        words.push_back(word);
    }

    for (int i = 0; i < M; ++i) {
        string plate; cin >> plate;
        int a = three[plate[0]-'A'][plate[1]-'A'][plate[2]-'A'];
        cout << (a == -1 ? "No valid word" : words[a]) << "\n";
    }
    return 0;
}
