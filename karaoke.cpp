#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi; 

int N;

int LIS(int N, vi &C) {
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

// find longest increasing subsequence and longest decreasing subsequence, take maximum
int main() {
    scanf("%d",&N);
    vi A(N, 0), B(N, 0);
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
        B[i] = -A[i];
    }
    printf("%d\n", max(LIS(N, A), LIS(N, B)));
    return 0;
}