#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef unordered_map<int,vi> miv;

int main() {
    ll n,m; scanf("%lld %lld",&n, &m);
    miv senders;
    ll total = 0;
    for (int i = 0; i < m; i++) {
        int s; scanf("%d",&s);
        total += n - 1;
        total -= (senders.find(s) == senders.end() ? i : i - senders[s].back() - 1);
        if (senders.find(s) == senders.end()) senders[s] = {i};
        else senders[s].push_back(i);
        printf("%lld\n",total);
    }
    return 0;
}