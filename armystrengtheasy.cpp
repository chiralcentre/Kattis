#include <bits/stdc++.h>
#include <queue>

using namespace std;

int main() {
    int T; scanf("%d",&T);
    while (T--) {
        int G,M; scanf("%d %d", &G, &M);
        priority_queue<int, vector<int>, greater<int>> g,m; //use min heap
        for (int i = 0; i < G; i++) {
            int a; scanf("%d",&a);
            g.push(a);
        } 
        for (int i = 0; i < M; i++) {
            int b; scanf("%d",&b);
            m.push(b);
        }
        while (!g.empty() && !m.empty()) {
            int a = g.top(), b = m.top();
            if (a < b) g.pop();
            else m.pop();
        }
        if (g.empty() && !m.empty()) printf("MechaGodzilla\n");
        else if (!g.empty() && m.empty()) printf("Godzilla\n");
        else printf("uncertain\n");
    }
    return 0;
}