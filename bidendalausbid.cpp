#include <bits/stdc++.h>

using namespace std;

int a,b,c,d;

int main() {
    scanf("%d:%d",&a,&b);
    scanf("%d:%d",&c,&d);
    int start = a * 60 + b;
    int end = c * 60 + d;
    int ans = end - start;
    if (ans < 0) ans += 1440;
    printf("%d\n",ans);
    return 0;
}