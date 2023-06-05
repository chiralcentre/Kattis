#include <bits/stdc++.h>

using namespace std;

int main() {
    // solve quadratic equation W^2 + (-2 - R/2)W + B + R = 0. take smaller value as W and larger value as L
    int R,B; scanf("%d %d",&R,&B);
    int b = -2 - R/2;
    int d = b * b - 4 * (B + R);
    int root = int(sqrt(d));
    if (root * root != d) root = (root - 1) * (root - 1) == d ? root - 1 : root + 1;
    int W = (-b - root) / 2;
    int L = (R + B) / W;
    printf("%d %d\n",L,W);
    return 0;
}