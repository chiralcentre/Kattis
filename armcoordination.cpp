#include <bits/stdc++.h>

using namespace std;

int x,y,r;

int main() {
    scanf("%d %d\n%d",&x,&y,&r);
    printf("%d %d\n",x - r,y - r);
    printf("%d %d\n",x + r,y - r);
    printf("%d %d\n",x + r,y + r);
    printf("%d %d\n",x - r,y + r);
    return 0;
}