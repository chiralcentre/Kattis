#include <bits/stdc++.h>

using namespace std;

char server[3];
int N, parts[3] = {0,0,0};

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 3; j++) {
            scanf(" %c",&server[j]); // space in front to avoid taking in spaces
            if (server[j] == 'J') parts[j]++;
        }
    }
    printf("%d\n", *min_element(parts, parts + 3));
    return 0;
}