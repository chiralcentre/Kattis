#include <bits/stdc++.h>

using namespace std;

int n,ta,da,tb,db;

int main() {
    scanf("%d\n%d %d\n%d %d",&n,&ta,&da,&tb,&db);
    int aliceTime = n * ta + da * ((n * (n - 1)) >> 1);
    int bobTime = n * tb + db * ((n * (n - 1)) >> 1);
    if (aliceTime < bobTime) printf("Alice\n");
    else if (aliceTime > bobTime) printf("Bob\n");
    else printf("=\n");
    return 0;
}