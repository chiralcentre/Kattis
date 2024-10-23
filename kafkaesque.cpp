#include <bits/stdc++.h>

using namespace std;

int N,c;

int main() {
    scanf("%d",&N);
    int prev = 0, passes = 1;
    scanf("%d",&prev);
    for (int i = 1; i < N; i++) {
        scanf("%d",&c);
        if (c < prev) passes++;
        prev = c;
    }
    printf("%d\n",passes);
    return 0;
}