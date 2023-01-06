#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
typedef tuple<int,ld,ld> idd;
typedef vector<int> vi;
typedef vector<idd> vidd;

//sort intervals by ascending order of left endpoint, and descending order of right endpoint
bool sortbyCond(const idd& a, const idd& b) {
    if (get<1>(a) != get<1>(b)) return get<1>(a) < get<1>(b);
    else return get<2>(a) > get<2>(b);
}

vi solve(vidd intervals, ld A, ld B) {
    vi ans;
    if (A == B) {
        for (idd p: intervals) {
            if (get<1>(p) <= A && get<2>(p) >= B) return vi {get<0>(p)};
        }
        return vi {};
    }
    if (get<1>(intervals[0]) > A) return ans;
    ld covered = A;
    for (int i = 0; i < intervals.size() && covered < B; i++) {
        if (get<2>(intervals[i]) < covered) continue; //inside previous interval
        if (get<1>(intervals[i]) > covered) {
            return vi {}; // discontinuity found
        } else {
            ld max_r = get<2>(intervals[i]) - 1.0;
            int max_id;
            //go to right to find interval with largest coverage
            for (int j = i; j < intervals.size() && get<1>(intervals[j]) <= covered; j++) {
                if (get<2>(intervals[j]) > max_r) {
                    max_r = get<2>(intervals[j]);
                    max_id = j;
                }
            }
            covered = max_r; i = max_id;
            ans.push_back(get<0>(intervals[max_id])); //insert original index
        }
    }
    if (covered < B) return vi {};
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ld A,B; int n;
    while (cin >> A >> B) {
        cin >> n;
        vidd intervals;
        for (int i = 0; i < n; i++) {
            ld a,b; cin >> a >> b;
            intervals.push_back(make_tuple(i,a,b));
        }
        sort(intervals.begin(),intervals.end(),sortbyCond);
        //for (idd p: intervals) printf("[%lf %lf] ",get<1>(p),get<2>(p));
        //printf("\n");
        vi ans = solve(intervals,A,B);
        if (ans.size() == 0) cout << "impossible" << "\n";
        else {
            cout << ans.size() << "\n";
            for (int i = 0; i < ans.size(); i++) {
                cout << ans[i];
                if (i < ans.size() - 1) cout << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}