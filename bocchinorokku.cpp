#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N;

int main() {
    scanf("%d", &N);
    vi rocks(N, 0), original(N, 0);
    for (int i = 0; i < N; i++) {scanf("%d",&rocks[i]); original[i] = rocks[i];}
    sort(rocks.begin(), rocks.end());
    unordered_map<int,int> mappings;
    for (int i = 0; i < N; i++) mappings[rocks[i]] = i;
    for (int i = 0; i < N; i++) {
        printf("%d", mappings[original[i]]);
        if (i < N - 1) printf(" ");
    }
    printf("\n");
    return 0;
}