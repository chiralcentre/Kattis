#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

int N, x, largest_multiplier[10001];
unordered_set<int> seen;

int main() {
    scanf("%d",&N);
    for (int i = 1; i <= 10000; i++) largest_multiplier[i] = 1;
    for (int i = 0; i < N; i++) {
        scanf("%d",&x);
        int m = largest_multiplier[x];
        while (seen.find(m * x) != seen.end()) m++;
        largest_multiplier[x] = m;
        int latest = m * x;
        seen.insert(latest);
        printf("%d\n",latest);
    }
    return 0;
}