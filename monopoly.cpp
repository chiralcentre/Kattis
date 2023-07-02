#include <bits/stdc++.h>

using namespace std;

//p[i] = probability of having a sum of i by rolling two dies
vector<double> p{0, 0, 1.0/36.0, 1.0/18.0, 1.0/12.0, 1.0/9.0, 5.0/36.0, 
                1.0/6.0, 5.0/36.0, 1.0/9.0, 1.0/12.0, 1.0/18.0, 1.0/36.0};
int N,A;

int main() {
    scanf("%d", &N);
    double ans = 0.0;
    for (int i = 0; i < N; i++) {
        scanf("%d", &A);
        ans += p[A];
    }
    printf("%lf\n",ans);
    return 0;
}