#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    scanf("%d",&N);
    vector<int> jobs(N,0), mappings(N,0);
    for (int i = 0; i < N; i++) {
        scanf("%d",&jobs[i]);
        jobs[i]--;
        mappings[jobs[i]] = i; // mappings[a] = b means that index b contains element a
    }
    int moves = 0;
    // put correct element into each index, swapping if necessary
    for (int i = 0; i < N; i++) {
        if (jobs[i] != i) {
            int num = jobs[i], other_index = mappings[i];
            swap(jobs[i], jobs[other_index]);
            moves++;
            // update new indices in mappings
            mappings[num] = other_index;
            mappings[i] = i;
        }
    }
    printf("%d\n",moves);
    return 0;
}