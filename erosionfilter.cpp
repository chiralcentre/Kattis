#include <bits/stdc++.h>

using namespace std;

typedef vector<double> vb;

int main() {
    int n; scanf("%d",&n);
    vb A(n,0),ps(n,0),ss(n,0);
    for (int i = 0; i < n; i++) scanf("%lf",&A[i]);
    ps[0] = A[0], ss[n - 1] = A[n - 1];
    // compute modified prefix sum array
    for (int i = 1; i < n; i++) ps[i] = ps[i - 1] / 2 + A[i];
    // compute modified suffix sum array
    for (int i = n - 2; i >= 0; i--) ss[i] = ss[i + 1] / 2 + A[i];
    for (int i = 0; i < n; i++) {
        printf("%lf", ps[i] + ss[i] - A[i]);
        if (i < n - 1) printf(" ");
    }
    return 0;
}