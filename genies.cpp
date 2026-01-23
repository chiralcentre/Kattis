#include <bits/stdc++.h>

using namespace std;

int W,K,C;

int main() {
    scanf("%d %d %d",&W,&K,&C);
    int H = 0, curr = K;
    while (curr > C) {
        H += curr - 1;
        curr -= C;
    }
    H += curr;
    (H >= W && W >= K) ? printf("yes\n") : printf("no\n");
    return 0;
}