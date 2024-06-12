#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N,a;

// a_i = bitwise OR of all m_ij for particular i satisfies properties of matrix
int main() {
    scanf("%d",&N);
    vi ans(N, 0);
    for (int i = 0; i < N; i++) {
        scanf("%d", &a);
        int first = a;
        for (int j = 1; j < N; j++) {
            scanf("%d",&a);
            first |= a;
        }
        ans[i] = first;
    }
    for (int i = 0; i < N - 1; i++) printf("%d ",ans[i]);
    printf("%d\n",ans[N - 1]);
    return 0;
}