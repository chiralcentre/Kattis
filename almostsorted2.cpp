#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int arr[300000];

string solve(int N) {
    // collapse all consecutive duplicates
    vi reduced; int k = 0;
    while (k < N) {
        reduced.push_back(arr[k]);
        int j = k;
        while (j < N - 1 && arr[j] == arr[j + 1]) j++;
        k = j + 1;
    }
    int s = -1, e = -1;
    for (int i = 0; i < reduced.size() - 1; i++) {
        if (reduced[i] > reduced[i + 1]) {
            //start of decreasing subarray not found yet
            if (s == -1) s = i;
            e = i + 1; // e stores the index of the element after the end of the decreasing subarray
        }
    }
    //if s == -1, array is sorted in increasing order
    //else, array has decreasing subsequence
    if (s != -1) {
        while (s < e) {
            swap(reduced[s], reduced[e]);
            s++;
            e--;
        }
        for (int i = 0; i < reduced.size() - 1; i++) {
            if (reduced[i] > reduced[i + 1]) return "No";
        }
    }
    return "Yes";
}

// idea: check for decreasing continuous array, reverse it and check if array is in ascending order
int main() {
    int N; scanf("%d",&N);
    for (int i = 0; i < N; i++) scanf("%d",&arr[i]);
    printf("%s\n", solve(N).c_str());
    return 0;
}