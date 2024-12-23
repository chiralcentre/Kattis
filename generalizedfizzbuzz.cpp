#include <bits/stdc++.h>

using namespace std;

int n,a,b;

int gcd(int e, int f) {
    while (f > 0) {
        int rem = e % f;
        e = f;
        f = rem;
    }
    return e;
}

int main() {
    scanf("%d %d %d",&n,&a,&b);
    int c = n / a;
    int d = n / b;
    int L = a / gcd(a, b) * b; // get LCM of a and b, divide by gcd first to prevent overflow
    int e = n / L;
    printf("%d %d %d\n",c - e,d - e,e);
    return 0;
}