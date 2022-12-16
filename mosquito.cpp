#include <bits/stdc++.h>

using namespace std;

int main() {
    int M,P,L,E,R,S,N;
    while(scanf("%d %d %d %d %d %d %d",&M,&P,&L,&E,&R,&S,&N) == 7) {
        for (int i = 0; i < N; i++) {
            int p = P;
            P = L / R;
            L = E * M;
            M = p / S;  
        }
        printf("%d\n",M);
    }
    return 0;
}