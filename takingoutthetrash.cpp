#include <bits/stdc++.h>

using namespace std;

int n,m,w;

int main() {
    multiset<int> trash;
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++) {
        scanf("%d",&w);
        trash.insert(w);
    }
    int trips = 0;
    while (!trash.empty()) {
        int lowest = *trash.begin();
        if (trash.size() >= 2) {
            int highest = *trash.rbegin();
            trash.erase(trash.find(highest));
            if (highest + lowest <= m) {
                trash.erase(trash.find(lowest));
            }
        } else {
            trash.erase(trash.find(lowest));
        }
        trips++;
    }
    printf("%d\n",trips);
    return 0;
}