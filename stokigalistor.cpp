#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int N; scanf("%d",&N);
    vi elems(N,0), sortedElems(N,0);
    for (int i = 0; i < N; i++) {
        scanf("%d",&elems[i]);
        sortedElems[i] = elems[i];
    }
    sort(sortedElems.begin(), sortedElems.end());
    int ans = 0;
    for (int i = 0; i < N; i++) ans += (elems[i] != sortedElems[i]);
    printf("%d\n",ans);
    return 0;
}