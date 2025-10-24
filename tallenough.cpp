#include <bits/stdc++.h>

using namespace std;

int n,h;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&h);
        if (h < 48) {
            printf("False\n");
            return 0;
        }
    }
    printf("True\n");
    return 0;
}