#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    int curr = 0;
    for (int i = 1; i <= n; i++) {
        curr += i;
        printf("%d\n",curr);
    }
    return 0;
}