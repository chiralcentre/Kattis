#include <bits/stdc++.h>
#include <set>

using namespace std;

typedef pair<int,int> ii;
typedef multiset<int> msi;

//maximum number of activities is 200000
ii activities[200000];
// sort by ascending order of end times, and tie break by ascending order of start times
struct sort_sec {
    bool operator() (ii &left, ii &right) {
        if (left.second == right.second) return left.first < right.first;
        return left.second < right.second;
    }
};

int main() {
    int n,k; scanf("%d %d",&n,&k);
    for (int i = 0; i < n; i++) {
        int u,v; scanf("%d %d",&u,&v);
        activities[i] = make_pair(u,v);
    }
    sort(activities, activities + n, sort_sec());
    int scheduled = 0;
    // multiset is used since multiple activities can have the same end time
    msi classrooms; 
    for (int i = 0; i < n; i++) {
        int s = activities[i].first, e = activities[i].second;
        // note that we want to find classroom with highest available time smaller than s
        // lower_bound in cpp gives the first element equivalent to or greater than s
        // Thus, to use lower_bound to achieve our goals, negation is required
        msi::iterator iter = classrooms.lower_bound(-s);
        // no suitable classroom found from current active classrooms, open new classrooms if available
        if (iter == classrooms.end()) {
            // can insert into new classroom
            if (classrooms.size() < k) {
                classrooms.insert(-e - 1); //offset by 1 since there are no overlap between activities
                scheduled++;
            }
        } else {
            // suitable classroom found from current active classrooms
            classrooms.erase(iter);
            classrooms.insert(-e - 1); 
            scheduled++;
        }
    }
    printf("%d\n",scheduled);
    return 0;
}