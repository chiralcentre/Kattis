#include <bits/stdc++.h>

using namespace std;

int w,s;

int main() {
    scanf("%d %d",&w,&s);
    int actual = ((s * (s + 1)) >> 1) * 29260;
    printf("%d\n",(w - actual) / 110);
    return 0;
}