#include <bits/stdc++.h>

using namespace std;

int a,b,s = 1;

int main() {
    for (int i = 0; i < 5; i++) {
        scanf("%d\n%d\n",&a,&b);
        if (s == a) s = b;
        else if (s == b) s = a;
    }
    printf("%d\n",s);
    return 0;
}