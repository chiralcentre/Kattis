#include <bits/stdc++.h>
#include <deque>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int main() {
    int N,C; scanf("%d %d",&N,&C);
    //normally two arrays are needed, but as A contains all 0s, only one array is needed, which doubles up as the difference array
    vll elems(N,0),A(N+1,0);
    for (int i = 0; i < N; i++) scanf("%lld",&elems[i]);
    int s = 0, e = 0;
    ll total = elems[0]; deque<ll> window {elems[0]};
    while (s <= N - 1) {
        if (s <= e) { A[s]++; A[e + 1]--;} //update range
        if (e > N - 2) s++;
        else if (s <= e && total + elems[e + 1] > C) {
            s++; total -= window.front(); window.pop_front();
        } else {
            e++; total += elems[e]; window.push_back(elems[e]);
        }
    }
    //print answer

    printf("%lld\n",A[0]);
    for (int i = 1; i < N; i++) {
        A[i] += A[i - 1];
        printf("%lld\n",A[i]);
    }
    return 0;
}