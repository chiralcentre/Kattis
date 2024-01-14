#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n; cin >> n;
    string s; cin >> s;
    long G = 0, total = 0, best = 0, prev_total = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] != 'D') total++;
        if (s[i] == 'G') G++;
        // check if G / total > best / prev_total
        if ((total > 0 && prev_total == 0) || G * prev_total > best * total) best = G, prev_total = total;
    }
    printf("%ld-%ld\n",best,prev_total - best);
    return 0;
}