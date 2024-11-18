#include <bits/stdc++.h>
#include <set>

using namespace std;

int n,a;

int main() {
    scanf("%d",&n);
    set<int> A1, A2, B1, B2;
    for (int i = 0; i < n; i++) {
        scanf("%d",&a);
        A1.insert(a);
        A2.insert(a);
    }
    for (int i = 1; i <= 2 * n; i++) {
        if (A1.find(i) == A1.end()) {
            B1.insert(i);
            B2.insert(i);
        }
    }
    // to find minimum number of matchings, repeatedly get the highest card for Alice and Bob, denoted as A and B respectively.
    // if A > B, win and pair A with lowest card for Bob, else if A < B, pair A and B. Equality case does not occur
    int min_match = 0;
    while (!A1.empty()) {
        int hA = *(A1.rbegin()), hB = *(B1.rbegin()), lB = *(B1.begin());
        if (hA > hB) {
            B1.erase(lB);
            min_match++;
        } else {
            B1.erase(hB);
        }
        A1.erase(hA);
    }

    // to find maximum number of matchings, repeatedly get the highest card for Alice and Bob, denoted as A and B respectively.
    // if A > B, get a win, else if A < B, pair B with lowest card for Alice. Equality case does not occur
    int max_match = 0;
    while (!A2.empty()) {
        int hA = *(A2.rbegin()), hB = *(B2.rbegin()), lA = *(A2.begin());
        if (hA > hB) {
            max_match++;
            A2.erase(hA);
        } else { // lA <= hA < hB
            A2.erase(lA); 
        }
        B2.erase(hB);
    }
    printf("%d %d\n",min_match,max_match);
    return 0;
}