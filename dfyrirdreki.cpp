#include <bits/stdc++.h>

using namespace std;

int a,b,c;

int main() {
    scanf("%d\n%d\n%d",&a,&b,&c);
    int d = b * b - 4 * a * c;
    if (d > 0) printf("2\n");
    else if (d == 0) printf("1\n");
    else printf("0\n");
    return 0;
}