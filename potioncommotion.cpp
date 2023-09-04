#include <bits/stdc++.h>

using namespace std;

int N,M,P,d;

// use greedy strategy: heal only when attack will take health to 0 or below
string solve() {
    int s = N;
    for (int i = 0; i < M; i++) {
        scanf("%d",&d);
        if (d < s) s -= d;
        else {
            if (d >= N) return "next time";
            int r = ceil((d + 1 - s) / 20.0);
            if (r > P) return "next time";
            else {
                P -= r;
                s += r * 20;
                s = min(s,N);
                s -= d;
            }
        }
    }
    return "champion";
}

int main() {
    scanf("%d %d %d",&N,&M,&P);
    printf("%s\n",solve().c_str());
    return 0;
}