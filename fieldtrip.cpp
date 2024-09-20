#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N, b;

int main() {
    scanf("%d",&N);
    vi prefixSum(N, 0);
    for (int i = 0; i < N; i++) { 
        scanf("%d",&b);
        prefixSum[i] = b;
        if (i > 0) prefixSum[i] += prefixSum[i - 1];
    }
    int total = prefixSum[N - 1];
    if (total % 3) printf("-1\n");
    else {
        int equalPart = total / 3, i = 0;
        while (i < N && prefixSum[i] < equalPart) i++;
        if (i == N || prefixSum[i] != equalPart) {
            printf("-1\n");
            return 0;
        }
        int j = i + 1;
        while (j < N && prefixSum[j] < (equalPart << 1)) j++;
        if (j == N || prefixSum[j] != (equalPart << 1)) {
            printf("-1\n");
            return 0;
        }
        printf("%d %d\n", i + 1, j + 1);
    }
    return 0;
}