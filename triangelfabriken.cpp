#include <bits/stdc++.h>

using namespace std;

int a,b,c;

int main() {
    scanf("%d\n%d\n%d",&a,&b,&c);
    int H = max(a,max(b,c));
    if (H > 90) printf("Trubbig Triangel\n");
    else if (H == 90) printf("Ratvinklig Triangel\n");
    else printf("Spetsig Triangel\n");
    return 0;
}