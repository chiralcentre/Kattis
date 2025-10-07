#include <bits/stdc++.h>

using namespace std;

int s;

int main() {
    scanf("%d",&s);
    if (s == -999) {
        printf("-500 -499\n");
    } else if (s == 999) {
        printf("500 499\n");
    } else if (s == 1) {
        printf("6 -5\n");
    } else if (s == -1) {
        printf("-6 5\n");
    } else printf("1 %d\n",s - 1);
    return 0;
}