#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int N,P; scanf("%d %d",&N,&P);
    int R = 300, solved = 0, penalty = 0;
    vi T;
    for (int i = 0; i < N; i++) {
        int t; scanf("%d",&t);
        if (i == P) {R -= t; penalty += t; solved++;}
        else T.push_back(t);
    }
    sort(T.begin(), T.end());
    if (R <= 0) printf("0 0\n");
    else {
        for (int t: T) {
            if (t <= R) {R -= t; penalty += 300 - R; solved++;}
            else break;
        }
        printf("%d %d\n",solved,penalty);
    }
    return 0;
}