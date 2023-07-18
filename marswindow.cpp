#include <bits/stdc++.h>

using namespace std;

int main() {
    int y; scanf("%d",&y);
    // months from Jan 2018
    int L = (y - 2018) * 12, H = L + 11;
    bool possible = (L <= ((H - 3) / 26) * 26 + 3 && ((H - 3) / 26) * 26 + 3  <= H);
    printf(possible ? "yes\n" : "no\n");
    return 0;
}