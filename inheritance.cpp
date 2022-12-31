#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef long long ll;
typedef queue<ll> qll;

int main() {
    ll N; scanf("%lld",&N);
    if (N % 2 == 0) {
        qll frontier;
        frontier.push(2);
        frontier.push(4);
        while (!frontier.empty() && frontier.front() <= N) {
            ll a = frontier.front();
            frontier.pop();
            if (N % a == 0) printf("%lld\n",a);
            a *= 10;
            if (a + 2 <= N) frontier.push(a + 2);
            if (a + 4 <= N) frontier.push(a + 4);
        }
    }
    return 0;
}