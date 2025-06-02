#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll A,B,C,D,E,X;

// there are three pathways to attain C starting from A
// 1. A -> B -> C
// 2. A -> C
// 3. A -> B -> E -> D -> B -> C
// As A can be used directly or indirectly to obtain C, let’s start by assuming A = 0 and start from converting B -> C. 
// Consider how to get the most C starting from initial B, D, E, X
// For path 3, 3E -> 2D -> 3B can be simplified to 3E -> 3B
// When B >= 3, we can perform the conversion 3B -> 4E and 3E -> 3B (one extra E per use of X)
// 9B -> 12E -> 8D -> 12B (4X required)
// Going from A → B → C requires 9 A for 1 C, whereas A → C directly needs only 5 A
// Unless you still have some X available, advancing A through B is a net loss.
// If X is still left, compare whether it’s more profitable to convert A into B or just follow path 1 to produce C.
int main() {
    scanf("%lld %lld %lld %lld %lld %lld",&A,&B,&C,&D,&E,&X);
    ll E_to_D = E / 3;
    E -= E_to_D * 3;
    D += E_to_D * 2;
    ll D_to_B = min(X, D / 2);
    D -= D_to_B * 2;
    B += D_to_B * 3;
    X -= D_to_B;
    // convert A to B only if the remainder modulus 3 >= 3
    if (A % 5 >= 3) {
        A -= 3;
        B++;
    }
    // going through path 1 and path 2 directly
    ll ans = A / 5 + B / 3 + C;
    
    // trying alternative pathway with 3B
    if (B < 3 && A >= (3 - B) * 3) {
        A -= (3 - B) * 3;
        B = 3;
    }
    if (B >= 3) {
        ll cycles = X / 4;
        B += 3 * cycles;
        X %= 4;
        if ((E == 2 && X >= 2) || (E == 1 && X >= 3))  {
            E = 0;
            B += 3;
            X = 0;
        }
        ans = max(ans, A / 5 + B / 3 + C);
    }
    printf("%lld\n",ans);
    return 0;
}