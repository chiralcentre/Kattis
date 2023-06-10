#include <bits/stdc++.h>

using namespace std;

int A,B,C,D,P,M,G;

string solve(int A, int B, int C, int D, int S) {
    int ans = 0;
    if (S % (A + B) <= A && S % (A + B) > 0) ans++;
    if (S % (C + D) <= C && S % (C + D) > 0) ans++;
    return (ans == 2) ? "both" : ((ans == 1) ? "one" : "none");
}

int main() {
    scanf("%d %d %d %d\n %d %d %d", &A, &B, &C, &D, &P, &M, &G);
    printf("%s\n",solve(A,B,C,D,P).c_str());
    printf("%s\n",solve(A,B,C,D,M).c_str());
    printf("%s\n",solve(A,B,C,D,G).c_str());
    return 0;
}