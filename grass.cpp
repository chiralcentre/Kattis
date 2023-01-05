#include <bits/stdc++.h>

using namespace std;

typedef pair<double,double> dd;
typedef vector<dd> vdd;


//sort intervals by ascending order of left endpoint, and descending order of right endpoint
bool sortbyCond(const dd& a, const dd& b) {
    if (a.first != b.first) return a.first < b.first;
    else return a.second > b.second;
}

int solve(vdd intervals, double l) {
    if (intervals[0].first > 0.0) return -1;
    double covered = 0.0; int ans = 0;
    for (int i = 0; i < intervals.size() && covered < l; i++) {
        dd p = intervals[i];
        if (p.second < covered) continue; //inside previous interval
        if (p.first > covered) {
            return -1; // discontinuity found
        } else {
            double max_r = -1.0;
            int max_id;
            //go to right to find interval with largest coverage
            for (int j = i; j < intervals.size() && intervals[j].first < covered; j++) {
                if (intervals[j].second > max_r) {
                    max_r = intervals[j].second;
                    max_id = j;
                }
            }
            ans++; covered = max_r; i = max_id;
        }
    }
    if (covered < l) return -1;
    return ans;
}

int main() {
    double n,l,w;
    //suppose a circle is centred at (x,y) with radius R
    //let dx = sqrt(R^2 - (W/2)^2)
    //interval covered by circle = [x - dx, x + dx]
    while (scanf("%lf %lf %lf",&n,&l,&w) == 3) {
        vdd intervals;
        for (int i = 0; i < n; i++) {
            double x,r; scanf("%lf %lf",&x,&r);
            if (2 * r > w) {// check if sprinkler can cover entire width 
                double dx = sqrt(r * r - (w / 2.0) * (w / 2.0));
                intervals.push_back(make_pair(x - dx, x + dx));
            }
        }
        sort(intervals.begin(),intervals.end(),sortbyCond);
        //printf("DEBUG\n");
        //for (dd p: intervals) printf("[%lf %lf] ",p.first,p.second);
        printf("%d\n",solve(intervals,l));
    }
    return 0;
}