#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

double greatCircleDistance(double pLa, double pLo, double qLa, double qLo, double r) {
    pLa *= M_PI/180; pLo *= M_PI/180;           // degree to radian
    qLa *= M_PI/180; qLo *= M_PI/180;
    return r * acos(cos(pLa)*cos(pLo)*cos(qLa)*cos(qLo) +
            cos(pLa)*sin(pLo)*cos(qLa)*sin(qLo) + sin(pLa)*sin(qLa));
}

int N;
double latitude[1000], longitude[1000], EPS = 1e-9;

// O(N^2) approach for each test case
int main() {
    while (scanf("%d\n",&N) == 1) {
        for (int i = 0; i < N; i++) scanf("%lf %lf",&latitude[i],&longitude[i]);
        double H = 1e9; int ans = -1;
        // find distance from each airport to every other airport
        for (int i = 0; i < N; i++) {
            double h = -1;
            for (int j = 0; j < N; j++) {
                if (i != j) {
                    double d = greatCircleDistance(latitude[i], longitude[i], latitude[j], longitude[j], 1);
                    h = max(d,h);
                }
            }
            if (abs(H - h) < EPS) ans = i;
            else if (h < H) {
                ans = i;
                H = h;
            }
        }
        printf("%.2lf %.2lf\n", latitude[ans], longitude[ans]);
    }
    return 0;
}