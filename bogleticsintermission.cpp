#include <bits/stdc++.h>

using namespace std;

int n,locations[100000],visited[100000];

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&locations[i]);
        locations[i]--; // offset by 1 for zero indexing
    }
    // answer = sum of lengths of all non trivial cycles + number of non trivial cycles
    int res = 0;
    for (int i = 0; i < n; i++) {
        if (locations[i] == i || visited[i]) continue;
        int curr = i;
        while (!visited[curr]) {
            visited[curr] = true;
            curr = locations[curr];
            res++;
        }
        res++;
    }
    printf("%d\n",res);
    return 0;
}