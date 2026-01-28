#include <bits/stdc++.h>

using namespace std;

int m,n;

int main() {
    while (true) {
        scanf("%d %d",&m,&n);
        if (m > n) printf("More\n");
        else if (m < n) printf("Less\n");
        else break;
    }
    return 0;
}