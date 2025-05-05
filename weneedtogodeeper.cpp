#include <bits/stdc++.h>

using namespace std;

int x,total = 0;

int main() {
    scanf("%d",&x);
    for (int i = 4; i <= 23; i++) {
        for (int j = 5; j <= 23; j++) {
            int used = 2 * j + 2 * i - 4;
            if (used <= x) total++;
            else break;
        }
    }
    printf("%d\n",total);
    return 0;
}