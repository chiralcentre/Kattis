#include <bits/stdc++.h>

using namespace std;

int N,steps = 0;

int main() {
    scanf("%d",&N);
    while (N > 1) {
        if (N % 2 == 1) N = N * 3 + 1;
        else N /= 2;
        steps++;
    }
    printf("%d\n", steps);
    return 0;
}