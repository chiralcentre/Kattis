#include <bits/stdc++.h>

using namespace std;

int n,m; string q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> q >> m;
    if (n > m) printf(">\n");
    else if (n < m) printf("<\n");
    else printf("Goggi svangur!\n");
    return 0;
}