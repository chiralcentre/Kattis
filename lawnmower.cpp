#include <bits/stdc++.h>

using namespace std;

typedef vector<double> vb;
int nx,ny; double w;

bool isFullLengthCovered(vb &cuts, double end, double w) {
    double start = 0.0;
    for (double x: cuts) {
        double nextStart = x - w / 2;
        if (nextStart > start) return false;
        start = x + w / 2;
    }
    return start >= end;
}

int main() {
    while (true) {
        scanf("%d %d %lf",&nx,&ny,&w);
        if (nx == 0 && ny == 0 && w == 0.0) break;
        vb h_cuts(nx, 0.0), v_cuts(ny, 0.0);
        for (int i = 0; i < nx; i++) scanf("%lf",&h_cuts[i]);
        for (int i = 0; i < ny; i++) scanf("%lf",&v_cuts[i]);
        sort(h_cuts.begin(), h_cuts.end());
        bool first_res = isFullLengthCovered(h_cuts, 75.0, w);
        if (!first_res) {
            printf("NO\n");
        } else {
            sort(v_cuts.begin(), v_cuts.end());
            bool second_res = isFullLengthCovered(v_cuts, 100.0, w);
            printf(second_res ? "YES\n" : "NO\n");
        }
    }
    return 0;
}