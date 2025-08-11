#include <bits/stdc++.h>

using namespace std;

int h,w,l,c;

int main() {
    scanf("%d %d %d %d",&h,&w,&l,&c);
    int v = h * w * l;
    if (v > c) printf("SO MUCH SPACE\n");
    else if (v == c) printf("COZY\n");
    else printf("TOO TIGHT\n");
    return 0;
}