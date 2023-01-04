#include <bits/stdc++.h>

using namespace std;

typedef pair<double,double> dd;
typedef vector<dd> vdd;

double distance(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

double f(double x, double y, vdd houses) {
    double ans = -1;
    for (dd pair: houses) {
        ans = max(ans, distance(pair.first,pair.second,x,y));
    }
    return ans;
}

int main() {
    double EPSILON = 0.00001;
    while (true) {
        int n; scanf("%d",&n);
        if (n == 0) break;
        vdd houses;
        for (int i = 0; i < n; i++) {
            double x,y; scanf("%lf %lf",&x,&y);
            houses.push_back(make_pair(x,y));
        }
        //perform ternary search
        double L = -200000, H = 200000;
        while (H - L > EPSILON) {
            double d = (H - L) / 3.0;
            double m1 = L + d, m2 = H - d;
            (f(m1,0,houses) > f(m2,0,houses)) ? L = m1 : H = m2;
        }
        double ans = (H + L) / 2.0;
        printf("%lf %lf\n",ans,f(ans,0,houses));
    }
    return 0;
}