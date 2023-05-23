#include <bits/stdc++.h>

using namespace std;

int main() {
    int C,K; scanf("%d %d",&C,&K);
    int B = int(pow(10,K)), R = C % B;
    (2 * R >= B) ? printf("%d\n", C + B - R) : printf("%d\n", C - R);
    return 0;
}