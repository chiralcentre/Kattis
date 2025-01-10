#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N; ll K,S;

unordered_map<ll,int> freq;

int main() {
    scanf("%d %lld",&N,&K);
    for (int i = 0; i < N; i++) {
        scanf("%lld",&S);
        ll comp = K - S;
        if (freq.find(comp) != freq.end()) {
            printf("%lld %lld\n",S,K - S);
            return 0;
        }
        freq[S]++;
    }
    printf("Neibb\n");
    return 0;
}