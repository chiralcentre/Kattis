#include <bits/stdc++.h>

using namespace std;

int v,n,k; char road[1000];

int main() {
    scanf("%d\n%d",&v,&n);
    while (n--) {
        scanf("%s %d",road,&k);
        printf("%s ",road);
        (v > k) ? printf("lokud\n") : printf("opin\n");
    }
    return 0;
}