#include <bits/stdc++.h>

using namespace std;

int a,b;

int main() {
    scanf("%d\n%d",&a,&b);
    int d = abs(a - b);
    printf("%d\n", min(d, 360 - d));
    return 0;
}