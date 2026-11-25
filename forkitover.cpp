#include <bits/stdc++.h>

using namespace std;

int n,b,p,saved = 0,bought = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&b,&p);
        saved += b - p;
        if (saved < 0) {
            bought -= saved;
            saved = 0;
        }
    }
    printf("%d\n",bought);
    return 0;
}