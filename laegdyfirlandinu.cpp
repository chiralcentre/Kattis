#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int n,m;

int main() {
    scanf("%d %d",&n,&m);
    vvi matrix(n, vi(m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d",&matrix[i][j]);
        }
    }
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < m - 1; j++) {
            if (matrix[i][j] < matrix[i - 1][j] && 
                matrix[i][j] < matrix[i + 1][j] &&
                matrix[i][j] < matrix[i][j - 1] &&
                matrix[i][j] < matrix[i][j + 1]) {
                printf("Jebb\n");
                return 0;
            }
        }
    }
    printf("Neibb\n");
    return 0;
}