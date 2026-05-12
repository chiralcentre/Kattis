#include <bits/stdc++.h>

using namespace std;

int n,pa,pb,a,b;

int main() {
    scanf("%d",&n);
    scanf("%d %d",&pa,&pb);
    for (int i = 0; i < n - 1; i++) {
        scanf("%d %d",&a,&b);
        if (a < pa || b < pb) {
            printf("no\n");
            return 0;
        }
        pa = a, pb = b;
    }
    printf("yes\n");
    return 0;
}