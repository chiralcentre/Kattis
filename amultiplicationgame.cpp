#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll p;

int main() {
    while(scanf("%lld",&p) == 1) {
        ll s = 1; 
        bool ollieTurn = true;
        while (s < p) {
            s *= (ollieTurn) ? 9 : 2;
            ollieTurn = !ollieTurn;
        }
        printf(ollieTurn ? "Ollie wins.\n": "Stan wins.\n");
    }
    return 0;
}