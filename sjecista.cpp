#include <bits/stdc++.h>

using namespace std;

// formula is n choose 4 for odd n
// since no three diagonals have the same intersection point, the same formula applies for all n
int main() {
    int n; scanf("%d",&n);
    printf("%d\n",n * (n - 1) * (n - 2) * (n - 3)/ 24);
    return 0;
}