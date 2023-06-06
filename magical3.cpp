#include <bits/stdc++.h>

using namespace std;

int n, MAX = 2147483647;

int main() {
    scanf("%d",&n);
    while (n != 0) {
        // solve for smallest x such that (n - 3) % x = 0, x >= 4
        if (n == 3) printf("4\n");
        else {
            int sol = MAX, r = n - 3;
            for (int i = 1; i <= int(sqrt(r)) + 1; i++) {
                if (r % i == 0) {
                    if (i >= 4) {
                        sol = min(sol, i);
                        break;
                    } else if (r / i >= 4) sol = min(sol, r / i);
                }
            }
            (sol != MAX) ? printf("%d\n",sol) : printf("No such base\n");
        }
        scanf("%d",&n);
    }
    return 0;
}