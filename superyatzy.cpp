#include <bits/stdc++.h>

using namespace std;

int N,M,t;
int die_count[6] = {0};

string solve(int M) {
    for (int i = 0; i < 6; i++) {
        if (N - die_count[i] <= M) return "Ja";
    }
    return "Nej";
}

int main() {
    scanf("%d %d",&N,&M);
    for (int i = 0; i < N; i++) {
        scanf("%d",&t);
        die_count[t - 1]++;
    }
    printf("%s\n",solve(M).c_str());
}