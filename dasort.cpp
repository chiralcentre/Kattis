#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

// minimum number of swaps is N - T, where T is the number of elements that appear after itself in unsorted array compared to sorted array
int main() {
    int P,s; scanf("%d",&P);
    while (P--) {
        int K,N; scanf("%d %d",&K,&N);
        vi unsorted(N,0), sorted(N,0);
        for (int i = 0; i < N; i++) {
            scanf("%d", &s);
            unsorted[i] = s;
            sorted[i] = s;
        }
        sort(sorted.begin(),sorted.end());
        int T = 0;
        for (int i = 0; i < N; i++) {
            if (sorted[T] == unsorted[i]) T++;
        }
        printf("%d %d\n",K,N - T);
    }
    return 0;
}