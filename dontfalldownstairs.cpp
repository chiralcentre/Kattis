#include <bits/stdc++.h>

using namespace std;

int N,p,c;

int main() {
    // note that the stairs are arranged in descending order, so there is never a need to add one brick to next step
    scanf("%d",&N);
    scanf("%d",&p);
    int effort = 0;
    for (int i = 0; i < N - 1; i++) {
        scanf("%d",&c);
        effort += max(0,p - c - 1);
        p = c;
    }
    effort += max(0,p - 1);
    printf("%d\n",effort);
    return 0;
}