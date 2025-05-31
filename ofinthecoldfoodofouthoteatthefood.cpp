#include <bits/stdc++.h>

using namespace std;

double T,H;

// final temperature is H
// amount of energy needed for food to cook is H * T
// suppose food is cooked for X minutes
// if X <= H, amount of energy food gets is X^2 / 2
// if X > H, amount of energy food gets is H^2 / 2 + (X - H) * H
// if H * T >= H^2 / 2, X = T + H / 2
// else, X = sqrt(2 * H * T)
int main() {
    scanf("%lf %lf",&T,&H);
    double p = H * T;
    if (p >= (H * H) / 2) printf("%lf\n", T + H / 2);
    else printf("%lf\n", sqrt(2 * p));
    return 0;
}