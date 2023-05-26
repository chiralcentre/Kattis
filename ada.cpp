#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

bool checkConstant(vi &seq) {
    for (int i = 0; i < seq.size() - 1; i++) {
        if (seq[i] != seq[i + 1]) return false;
    }
    return true;
}

int main() {
    int n; scanf("%d",&n);
    vvi seqs;
    vi curr(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&curr[i]);
    seqs.push_back(curr);
    while (!checkConstant(curr)) {
        vi temp(curr.size() - 1, 0);
        for (int i = 0; i < curr.size() - 1; i++) temp[i] = curr[i + 1] - curr[i];
        curr = temp;
        seqs.push_back(curr);
    }
    // extend the differences table
    seqs.back().push_back(seqs.back().back());
    for (int i = seqs.size() - 2; i >= 0; i--) seqs[i].push_back(seqs[i].back() + seqs[i + 1].back());
    printf("%d %d",seqs.size() - 1, seqs[0].back());
    return 0;
}