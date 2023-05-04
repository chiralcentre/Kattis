#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int k1,k2; scanf("%d",&k1);
    vi A(k1,0);
    for (int i = 0; i < k1; i++) scanf("%d",&A[i]);
    scanf("%d",&k2);
    vi B(k2,0);
    for (int i = 0; i < k2; i++) scanf("%d",&B[i]);
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    //turn = -1 means havent started or both people liked the movie
    //turn = 1 means only first person liked the movie previously
    //turn = 0 means only second person liked the movie previously
    int i = 0, j = 0, ans = 0, turn = -1;
    while (i < k1 && j < k2) {
        if (A[i] < B[j]) {
            i++;
            if (turn == -1 || turn == 0) {
                ans++;
                turn = 1;
            }
        } else if (A[i] == B[j]) {
            i++; j++;
            ans++;
            turn = -1;
        } else { // A[i] > B[j]
            j++;
            if (turn == -1 || turn == 1) {
                ans++;
                turn = 0;
            }
        }
    }
    if (i != k1 || j != k2) {
        if (turn = -1) ans++;
    }
    printf("%d\n", ans);
    return 0;
}