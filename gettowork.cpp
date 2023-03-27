#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

void solve(vvi &cities, vi &employees, vi &commute, int N, int T) {
    for (int j = 0; j < N; j++) {
        if (j == T) continue;
        sort(cities[j].begin(), cities[j].end());
        while (employees[j] > 0 && !cities[j].empty()) {
            employees[j] -= cities[j].back();
            cities[j].pop_back();
            commute[j]++;
        }
        if (employees[j] > 0) {printf("IMPOSSIBLE\n"); return;}
    }
    for (int i = 0; i < N; i++) {
        printf("%d", commute[i]);
        if (i < N - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    int TC; scanf("%d",&TC);
    for (int i = 0; i < TC; i++) {
        int N,T,E;
        scanf("%d %d",&N,&T); scanf("%d",&E);
        vvi cities(N,vi {}); 
        vi employees(N,0), commute(N,0);
        for (int j = 0; j < E; j++) {
            int H,P; scanf("%d %d",&H,&P);
            employees[H - 1]++;
            if (P > 0) cities[H - 1].push_back(P);
        }
        printf("Case #%d: ", i + 1);
        solve(cities, employees, commute, N, T - 1);
    }
    return 0;
}