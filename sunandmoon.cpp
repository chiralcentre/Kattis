#include <bits/stdc++.h>

using namespace std;

int main() {
    int ds,ys,dm,ym; scanf("%d %d\n%d %d",&ds,&ys,&dm,&ym);
    int d = 0;
    //maximum 5000 iterations
    while ((ds + d) % ys != 0 || (dm + d) % ym != 0) d++;
    printf("%d\n",d);
    return 0;
}