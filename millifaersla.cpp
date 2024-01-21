#include <bits/stdc++.h>

using namespace std;

int a,b,c;

int main() {
    scanf("%d\n%d\n%d",&a,&b,&c);
    if (a < b && a < c) printf("Monnei\n");
    else if (b < a && b < c) printf("Fjee\n");
    else printf("Dolladollabilljoll\n");
    return 0;
}