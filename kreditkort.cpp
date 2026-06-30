#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    if (n <= 500) printf("500\n");
    else if (n <= 1000) printf("1000\n");
    else if (n <= 2000) printf("2000\n");
    else if (n <= 5250) printf("5000\n");
    else if (n <= 11000) printf("10000\n");
    else if (n <= 24000) printf("20000\n");
    return 0;
}