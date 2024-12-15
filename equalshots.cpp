#include <bits/stdc++.h>

using namespace std;

int a,b,v,c;

int main() {
    scanf("%d %d",&a,&b);
    int v1 = 0, v2 = 0;
    for (int i = 0; i < a; i++) {
        scanf("%d %d",&v,&c);
        v1 += v * c;
    }
    for (int i = 0; i < b; i++) {
        scanf("%d %d",&v,&c);
        v2 += v * c;
    }
    (v1 == v2) ? printf("same\n") : printf("different\n");
    return 0;
}