#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi; 

int N, C[500000];

int LIS(int N) {
    vi L; L.push_back(C[0]);
    for (int i = 1; i < N; i++) {
        //add to LIS
        if (C[i] > L.back()) L.push_back(C[i]);
        //replace with better candidate
        else {
            int pos = lower_bound(L.begin(), L.end(), C[i]) - L.begin();
            L[pos] = C[i];
        }
    }
    return L.size();
}

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) scanf("%d", &C[i]);
    printf("%d\n", LIS(N));
    return 0;
}
