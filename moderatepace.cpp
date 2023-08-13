#include <bits/stdc++.h>

using namespace std;

int A[1000],B[1000],C[1000],n;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) scanf("%d",&A[i]);
    for (int i = 0; i < n; i++) scanf("%d",&B[i]);
    for (int i = 0; i < n; i++) scanf("%d",&C[i]);
    for (int i = 0; i < n; i++) {
        vector<int> temp = {A[i], B[i], C[i]};
        sort(temp.begin(),temp.end());
        printf("%d",temp[1]); // take median
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}