#include <bits/stdc++.h>

using namespace std;

int N,g,b,t = 0;

int main() {
    scanf("%d",&N);
    while (N--) {
        scanf("%d %d",&g,&b);
        t += g;
        if (t < b) {
            printf("impossible\n");
            return 0;
        }
    }
    printf("possible\n");
    return 0;
}