#include <bits/stdc++.h>

using namespace std;

int arr[300000];

string solve(int N) {
    int s = -1, e = -1;
    for (int i = 0; i < N - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            //start of decreasing subarray not found yet
            if (s == -1) s = i;
            e = i + 1; // e stores the index of the element after the end of the decreasing subarray
        }
    }
    //if s == -1, array is sorted in increasing order
    //else, array has decreasing subsequence
    if (s != -1) {
        reverse(arr + s, arr + e + 1);
        for (int i = 0; i < N - 1; i++) {
            if (arr[i] > arr[i + 1]) return "No";
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