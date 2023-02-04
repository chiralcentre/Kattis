#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
    int N; scanf("%d",&N);
    vvi adjMat(N,vi(N,0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d",&adjMat[i][j]);
        }
    }
    int counter = 0;
    //O(N^3) loop
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                if (adjMat[i][j] + adjMat[j][k] + adjMat[k][i] == 3) counter++;
            }
        }
    }
    printf("%d\n",counter);
    return 0;
}