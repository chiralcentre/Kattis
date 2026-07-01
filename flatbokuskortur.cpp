#include <bits/stdc++.h>

using namespace std;

int x,y,z;

int main() {
    scanf("%d\n%d\n%d",&x,&y,&z);
    x * x <= y * y * z ? printf("Jebb\n") : printf("Neibb\n");
    return 0;
}