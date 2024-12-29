#include <bits/stdc++.h>

using namespace std;

int n; string temp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int expenses = 0;
    getline(cin, temp);
    n = stoi(temp);
    for (int i = 0; i < n; i++) {
        getline(cin, temp);
        getline(cin, temp);
        expenses += stoi(temp);
    }
    if (expenses > 0) printf("Usch, vinst\n");
    else if (expenses == 0) printf("Lagom\n");
    else printf("Nekad\n");
    return 0;
}