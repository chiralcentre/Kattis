#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;

int n,a;

// O(n log n) while ensuring descending vector
int main() {
    scanf("%d",&n);
    vi seqs;
    for (int i = 0; i < n; i++) {
        scanf("%d",&a);
        // lower_bound for descending vector return index of first element <= target
        int index = lower_bound(seqs.begin(), seqs.end(), a, greater<int>()) - seqs.begin();
        // a is smaller than all elements in seqs
        if (index == seqs.size()) seqs.push_back(a);
        else seqs[index] = a;
    }
    printf("%d\n", seqs.size());
    return 0;
}