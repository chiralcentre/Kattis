#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef vector<int> vi;

int n,k,a;

// code runs in O(n log n);
int main() {
    scanf("%d %d", &n, &k);
    // use min heap
    priority_queue<int, vi, greater<int>> dogs;
    scanf("%d",&a);
    dogs.push(a);
    for (int i = 1; i < n; i++) {
        scanf("%d",&a);
        int lowest = dogs.top();
        if (lowest + k <= a) dogs.pop();
        dogs.push(a);
    }
    printf("%d\n", dogs.size());
    return 0;
}