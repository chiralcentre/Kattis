#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

int N,n,l,d,g;

int main() {
    scanf("%d",&N);
    while (N--) {
        scanf("%d %d %d %d",&n,&l,&d,&g);
        // let a be length of apothem, and p be perimeter
        double p = n * l;
        double a = double(l) / (2 * tan(M_PI / n));
        // break down area into original polygon, n rectangles of length g * d and width l, and a circle with radius d * g
        double area = p * a / 2 + n * g * d * l + d * g * d * g * M_PI;
        printf("%lf\n",area);
    }
    return 0;
}