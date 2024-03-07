#include <bits/stdc++.h>

using namespace std;

int n, d;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < 3; i++) {
        bool seen = false;
        for (int j = 0; j < n; j ++) {
            scanf("%d",&d);
            if (d == 7) seen = true;
        }
        if (!seen) {
            printf("0\n");
            return 0;
        }
    }
    printf("777\n");
    return 0;
}