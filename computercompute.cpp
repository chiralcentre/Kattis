#include <bits/stdc++.h>

using namespace std;

double x1,y,x2,y2;

int main() {
    scanf("%lf\n%lf\n%lf\n%lf",&x1,&y,&x2,&y2);
    printf("%lf\n",sqrt((x1 - x2) * (x1 - x2) + (y - y2) * (y - y2)));
    return 0;
}