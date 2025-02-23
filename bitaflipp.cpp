#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int n,total = 0;

// find maximum sum of contiguous subarray using Kadane's algorithm in O(n) time
int main() {
    scanf("%d",&n);
    vi cells(n, 0);
    for (int i = 0; i < n; i++) {
        scanf("%d",&cells[i]);
        total += cells[i];
        cells[i] = (cells[i] == 1) ? -1 : 1;
    }
    int curr = 0, mx = -1;
    for (int i = 0; i < n; i++) {
        curr = max(cells[i], curr + cells[i]);
        mx = max(mx, curr);
    }
    printf("%d\n", total + mx);
    return 0;
}