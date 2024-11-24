#include <bits/stdc++.h>

using namespace std;

int getPrimeFactor(int n) {
    for (int s = 2; s * s <= n; s++) {
        if (n % s == 0) return s;
    }
    return -1;
}

int n;

int main() {
    scanf("%d",&n);
    // if n is even, one crate is sufficient
    if (n % 2 == 0) printf("2x%d\n",n / 2);
    else {
        if (n == 3 || n == 5 || n == 7 || n == 11) printf("impossible\n");
        else {
            int pf = getPrimeFactor(n);
            if (pf == -1) { // prime number
            // note n - 9 is guaranteed to be even
                printf("3x3 2x%d\n",(n - 9) / 2);
            } else {
                printf("%dx%d\n",pf,n / pf);
            }
        }
    }
    return 0;
}