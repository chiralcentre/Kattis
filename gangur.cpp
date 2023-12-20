#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    vll right,left;
    for (ll i = 0; i < s.length(); i++) {
        if (s[i] == '>') right.push_back(i);
        else if (s[i] == '<') left.push_back(i);
    }
    // for every > character, check how many < characters are there in front of it
    // O(N log N) where N is length of string
    ll ans = 0;
    for (ll r: right) {
        ll index = lower_bound(left.begin(), left.end(), r) - left.begin();
        if (index < left.size()) ans += left.size() - index;
    }
    printf("%lld\n",ans);
    return 0;
}