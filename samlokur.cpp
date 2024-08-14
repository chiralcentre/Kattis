#include <bits/stdc++.h>
#include <map>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int n,k;

string solve(int k, vvi &avail_sandwiches) {
    // start from highest timeslot since sandwiches can be served at any time before that
    // for every possible timeslot, take highest quality sandwich, and smallest quality sandwich, and check that their combined qualities >= 9
    // algorithm runs in O(N log N) time
    map<int,int> counter;
    for (int i = k - 1; i >= 0; i--) {
        // if sandwich exists in counter, increment frequency by 1, else initialise with default value of 0 and increase by 1
        for (int s: avail_sandwiches[i]) counter[s]++;
        if (!counter.empty()) {
            auto smallestEntry = *counter.begin();
            int firstSandwich = smallestEntry.first;
            counter[firstSandwich]--;
            if (counter[firstSandwich] == 0) counter.erase(firstSandwich);
            if (!counter.empty()) {
                auto largestEntry = *counter.rbegin();
                int secondSandwich = largestEntry.first;
                counter[secondSandwich]--;
                if (counter[secondSandwich] == 0) counter.erase(secondSandwich);
                if (firstSandwich + secondSandwich < 9) return "Neibb";
            } else {
                return "Neibb";
            }
        } else {
            return "Neibb";
        }
    }
    return "Jebb";
}

int main() {
    scanf("%d %d",&n,&k);
    vi a(n, 0), b(n, 0);
    // avail_sandwiches[i] contains all the sandwiches that expire on day i
    vvi avail_sandwiches(k, vi {});
    for (int i = 0; i < n; i++) scanf("%d",&a[i]);
    for (int i = 0; i < n; i++) { scanf("%d",&b[i]); b[i]--; } // offset by 1 due to zero indexing
    int available = 0;
    for (int i = 0; i < n; i++) {
        // only keep track of sandwiches with quality >= 4
        if (a[i] >= 4) {
            available++;
            int d = min(b[i], k - 1);
            if (d >= 0) avail_sandwiches[d].push_back(a[i]);
        }
    }
    
    available >= 2 * k ? printf("%s\n", solve(k, avail_sandwiches).c_str()) : printf("Neibb\n");
    return 0;
}