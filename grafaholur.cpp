#include <bits/stdc++.h>

using namespace std;

double n,h,x,m,y;

int main() {
    scanf("%lf\n%lf\n%lf\n%lf\n%lf\n",&n,&h,&x,&m,&y);
    printf("%lf\n", (h * n * y) / (x * m));
    return 0;    
}