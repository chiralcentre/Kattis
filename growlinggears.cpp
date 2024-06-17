#include <bits/stdc++.h>

using namespace std;

int T,n; double a,b,c;

double calculate(double x) {
    return - a * x * x + b * x + c;
}

int main() {
    scanf("%d",&T);
    for (int i = 0; i < T; i++) {
        scanf("%d",&n);
        double best = -1; int ans = -1;
        for (int j = 0; j < n; j++) {
            scanf("%lf %lf %lf",&a,&b,&c);
            // T = -aR^2 + bR + c
            // dT/dR = -2aR + b
            // dT/dR = 0 -> R = b / 2a
            double result = calculate(b / (2 * a));
            if (result > best) {
                best = result;
                ans = j + 1;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}