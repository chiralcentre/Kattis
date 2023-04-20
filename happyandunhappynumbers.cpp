#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef unordered_set<int> usi;
int happy[1000001];

int sumSquare(int n) {
    int t = 0;
    while (n > 0) {
        int d = n % 10;
        t += d * d;
        n /= 10;
    }
    return t;
}

int checkHappy(int n) {
    usi seen;
    while (n > 9) {
        n = sumSquare(n);
        if (seen.find(n) != seen.end()) return 0;
        seen.insert(n);
    }
    return (n == 1 || n == 7) ? 1 : 0;
}

int main() {
    //precompute
    happy[0] = 0;
    for (int i = 1; i < 1000001; i++) happy[i] = happy[i - 1] + checkHappy(i);
    int T; scanf("%d",&T);
    while (T--) {
        int A,B; scanf("%d %d",&A,&B);
        printf("%d\n",happy[B] - happy[A - 1]);
    }
    return 0;
}