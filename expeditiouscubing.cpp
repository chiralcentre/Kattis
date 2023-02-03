#include <bits/stdc++.h>

using namespace std;

int solve(int t1, int t2, int t3, int t4, int total) {
    //there are five possible insertion points of fifth time
    //case 1: new time is inserted before t1, and new time,t4 are discarded
    if (t1 + t2 + t3 > total) return -1;
    //case 2: new time is inserted after t4, t1, new time are discarded
    if (t2 + t3 + t4 <= total) return -2;
    /*case 3: new time is inserted in between t1 and t2, t1,t4 are discarded
    case 4: new time is inserted in between t2 and t3, t1,t4 are discarded
    case 5: new time is inserted in between t3 and t4, t1,t4 are discarded */
    return total - t2 - t3;
}

int main() {
    int p1,p2,p3,p4,p5,p6,p7,p8,p9,p10;
    scanf("%d.%d",&p1,&p2);
    scanf("%d.%d",&p3,&p4);
    scanf("%d.%d",&p5,&p6);
    scanf("%d.%d",&p7,&p8);
    scanf("%d.%d",&p9,&p10);
    int t1 = p1 * 100 + p2, t2 = p3 * 100 + p4;
    int t3 = p5 * 100 + p6, t4 = p7 * 100 + p8;
    int total = (p9 * 100 + p10) * 3;
    vector<int> timings {t1,t2,t3,t4};
    sort(timings.begin(), timings.end());
    t1 = timings[0], t2 = timings[1], t3 = timings[2], t4 = timings[3];
    int ans =  solve(t1,t2,t3,t4,total);
    double counter = (double) ans / 100.0;
    if (ans == -1) cout << "impossible\n";
    else if (ans == -2) cout << "infinite\n";
    else cout << fixed << setprecision(2) << counter << "\n";
    return 0;
}