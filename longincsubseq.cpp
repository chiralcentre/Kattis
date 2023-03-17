#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int A[100000];

void print_LIS_indices(vi &p, int i) {
    if (p[i] == -1) {printf("%d",i); return;}
    print_LIS_indices(p,p[i]);
    printf(" %d", i);
}

void LIS(int N) {
    vi L(N,0), indices(N,0), p(N,-1);
    int k = 0, LIS_end = 0;
    for (int i = 0; i < N; i++) {
        int pos = lower_bound(L.begin(), L.begin() + k, A[i]) - L.begin();
        L[pos] = A[i];
        indices[pos] = i;
        p[i] = pos ? indices[pos - 1] : -1;
        if (pos == k) {
            k = pos + 1;
            LIS_end = i;
        }
        /*
        printf("L = ");
        for (int p: L) printf("%d ",p);
        printf("\n");
        printf("Indices = ");
        for (int p: indices) printf("%d ",p);
        printf("\n"); */
    }
    printf("%d\n", k);
    print_LIS_indices(p,LIS_end);
    printf("\n");
}

int main() {
    int N;
    while (scanf("%d",&N) == 1) {
        for (int i = 0; i < N; i++) scanf("%d",&A[i]);
        LIS(N);
    }
    return 0;
}