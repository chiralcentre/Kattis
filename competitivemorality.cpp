#include <bits/stdc++.h>

using namespace std;

int R,B;

int main() {
    scanf("%d\n%d",&R,&B);
    (B == R || B == R - 1) ? printf("BLUE\n") : printf("RED\n");
    return 0;
}