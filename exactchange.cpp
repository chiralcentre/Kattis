#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    scanf("%d",&N);
    int a = 0, b = 0, c = 0, d = 0, e = 0;
    if (N >= 150) {
        e = N / 150;
        N %= 150;
    }
    if (N >= 30) {
        d = N / 30;
        N %= 30;
    }
    if (N >= 15) {
        c = N / 15;
        N %= 15;
    }
    if (N >= 5) {
        b = N / 5;
        N %= 5;
    }
    if (N >= 1) {
        a = N;
        N = 0;
    }
    printf("%d %d %d %d %d\n",a,b,c,d,e);
    return 0;
}