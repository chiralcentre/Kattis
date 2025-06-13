#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N;

// In the first pass, let us go through the users in the increasing order of tier and try to assign slots in a lower tier to everybody.
// If we have multiple options, we choose the slot with a higher number (as close as possible to the target tier, but still lower than it). 
// If we cannot do it, we skip the user for now.
// Having done those assignments we can no longer get any additional +1 scores, so we should
// focus on getting on as many 0 scores as possible. In order to do this, we run a second pass over
// all tiers and assign as many users to their target tier as possible.

int main() {
    scanf("%d",&N);
    vi x(N, 0), y(N, 0);
    for (int i = 0; i < N; i++) scanf("%d",&x[i]);
    for (int i = 0; i < N; i++) scanf("%d",&y[i]);
    int good = 0, okay = 0, bad = 0, avail = 0;
    for (int i = 0; i < N; i++) {
        // assign users from a higher tier to a lower tier
        int a = min(y[i], avail);
        avail -= a; y[i] -= a; good += a;
        
        // assign later
        a = min(y[i], okay);
        okay -= a; bad += a; good += a; y[i] -= a;
        
        // assign users to same tier
        a = min(y[i], x[i]);
        okay += a; y[i] -= a; x[i] -= a;
        avail += x[i];
        bad += y[i];
    }
    printf("%d\n", good - bad);
    return 0;
}