#include <bits/stdc++.h>

using namespace std;

int N, k;

int main() {
    scanf("%d", &N);
    unordered_set<int> seen;
    for (int i = 0; i < N; i++) {
        scanf("%d", &k);
        if (seen.find(k) == seen.end()) {
            seen.insert(k);
            printf("1");
        } else printf("0");
        if (i < N - 1) printf(" ");
    }
    return 0;
}