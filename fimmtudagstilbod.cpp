#include <bits/stdc++.h>

using namespace std;

int y;

int main() {
    scanf("%d",&y);
    printf("%d\n",max(0,y - 2020) * 100 + 1000);
    return 0;
}