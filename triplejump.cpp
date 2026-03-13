#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    vector<int> D(n, 0);
    for (int i = 0; i < n; i++) scanf("%d",&D[i]);
    // smallest jump is smallest triple jump divided by 3
    // largest jump is largest triple jump divided by 3
    // middle jump is second smallest triple jump - 2 * smallest jump
    int a = D[0] / 3;
    int b = D[1] - a * 2;
    int c = D[n - 1] / 3;
    printf("%d %d %d\n",a,b,c);
    return 0;
}