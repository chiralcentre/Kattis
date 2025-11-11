#include <bits/stdc++.h>

using namespace std;

int k,s;

int main() {
    scanf("%d %d",&k,&s);
    printf("%d\n", s / k + s % k);
    return 0;
}