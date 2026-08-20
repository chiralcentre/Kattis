#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    if (n <= 999) printf("Invalid");
    else if (n < 2400) printf("Amateur");
    else if (n < 2500) printf("International grandmaster");
    else if (n < 2700) printf("Grandmaster");
    else printf("Super grandmaster");
    return 0;
}