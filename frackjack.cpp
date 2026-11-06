#include <bits/stdc++.h>

using namespace std;

int A,B;

int main() {
    scanf("%d\n%d",&A,&B);
    if (A == B || (A > 21 && B > 21)) printf("Jack\n");
    else if (A > 21 && B <= 21) printf("Bertil\n");
    else if (A <= 21 && B > 21) printf("Alice\n");
    else printf(A > B ? "Alice\n" : "Bertil\n");
    return 0;
}