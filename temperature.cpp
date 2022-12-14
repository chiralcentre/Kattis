#include <bits/stdc++.h>

using namespace std;

int main() {
    int X,Y; scanf("%d %d",&X,&Y);
    printf(Y == 1 ? (X == 0 ? "ALL GOOD\n" : "IMPOSSIBLE\n") : "%f\n", (double) X / (double) (1-Y));
    return 0;
}