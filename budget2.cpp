#include <bits/stdc++.h>

using namespace std;

int b,p1,p2,p3;

int main() {
    scanf("%d\n%d\n%d\n%d",&b,&p1,&p2,&p3);
    printf((b >= p1 + p2 + p3) ? "Budget is sufficient.\n" : "Budget is insufficient.\n");
    return 0;
}