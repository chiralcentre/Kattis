#include <bits/stdc++.h>

using namespace std;

int x;
const int HOUR = 3600;

int main() {
    scanf("%d",&x);
    int r = HOUR - x % HOUR;
    printf("%d\n", r / 60 + (r % 60 > 0));
    return 0;
}