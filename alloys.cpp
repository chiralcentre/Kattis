#include <bits/stdc++.h>

using namespace std;

int main() {
    // cannot exceed paying $1 per kilogram since x + y + z = 1
    // to maximise xy, let x = y
    double c; scanf("%lf",&c);
    printf("%lf\n",min(0.25, c/2 * c/2));
    return 0;
}