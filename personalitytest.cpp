#include <bits/stdc++.h>

using namespace std;

int n,a;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        vector<int> freq(4,0);
        for (int j = 0; j < 20; j++) {
            scanf("%d",&a);
            freq[a - 1]++;
        }
        int best = -1, high = -1;
        for (int k = 0; k < 4; k++) {
            if (freq[k] > high) {
                high = freq[k];
                best = k;
            }
        }
        if (best == 0) printf("leader\n");
        else if (best == 1) printf("intellectual\n");
        else if (best == 2) printf("social\n");
        else printf("practical\n");
    }
    return 0;
}