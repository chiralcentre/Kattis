#include <bits/stdc++.h>

using namespace std;

int e,m;
int ce = 1;

int main() {
    while (scanf("%d %d",&e,&m) == 2) {
        int c = 0;
        while (e != 0 || m != 0) {
            e = (e + 1) % 365;
            m = (m + 1) % 687;
            c++;
        }
        printf("Case %d: %d\n",ce++,c);
    }
    return 0;
}