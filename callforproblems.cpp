#include <bits/stdc++.h>

using namespace std;

int n,d,counter = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&d);
        counter += (d % 2 == 1);
    }
    printf("%d\n",counter);
    return 0;
}