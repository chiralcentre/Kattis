#include <bits/stdc++.h>
#include <string>

using namespace std;

const int MAX_N = 303;
string ans = "NO";
bool gaps[MAX_N], visited[MAX_N][MAX_N][MAX_N];
int counter = 0;

void solve(int c1, int c2, int c3, int curr) {
    visited[c1][c2][c3] = true;
    if (ans == "YES" || curr > counter) return;
    if (curr == counter) {
        ans = "YES";
        return;
    }
    if (!gaps[curr + 1] && c1 > 0 && !visited[c1 - 1][c2][c3]) solve(c1 - 1,c2,c3,curr + 1);
    if (!gaps[curr + 2] && c2 > 0 && !visited[c1][c2 - 1][c3]) solve(c1,c2 - 1,c3,curr + 2);
    if (!gaps[curr + 3] && c3 > 0 && !visited[c1][c2][c3 - 1]) solve(c1,c2,c3 - 1,curr +3);
}

int main() {
    int N,c1,c2,c3; scanf("%d %d %d %d",&N,&c1,&c2,&c3);
    for (int i = 0; i < N; i++) {
        int a; scanf("%d",&a);
        counter += a;
        if (i < N  - 1) gaps[counter] = true;
    }
    solve(c1,c2,c3,0);
    printf("%s\n",ans.c_str());
    return 0;
}