#include <bits/stdc++.h>

using namespace std;

int x,y,z;

int main() {
    scanf("%d %d %d",&x,&y,&z);
    int total = x * 25 + y * 25 + z * 50;
    if (total >= 9000) {
        printf("A\n");
    } else if (total >= 8000) {
        printf("B\n");
    } else if (total >= 7000) {
        printf("C\n");
    } else if (total >= 6000) {
        printf("D\n");
    } else {
        printf("F\n");
    }
    return 0;
}