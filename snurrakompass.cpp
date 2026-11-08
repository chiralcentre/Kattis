#include <bits/stdc++.h>

using namespace std;

int a,b;

int main() {
    scanf("%d\n%d",&a,&b);
    // everything reachable is a multiple of g
    // actual position after x moves of first arm and y moves of second arm, P = ax + by - 360z, for some integer z
    // P is divisible by g by definition
    // g is reachable by Bezout's identity
    int g = gcd(gcd(a,b), 360);
    printf("%d\n", 360 / g);
    return 0;
}