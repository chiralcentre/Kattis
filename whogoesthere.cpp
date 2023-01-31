#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int n,m; scanf("%d %d",&n,&m);
    vi accepted(m,0), sent(m,0);
    int total = 0;
    for (int i = 0; i < m; i++) {scanf("%d",&sent[i]); total += sent[i];}
    int H = min(n,total); 
    //code runs in O(n)
    for (int i = 0; H > 0; i = (i + 1) % m) {
        if (sent[i] > 0) {accepted[i]++; sent[i]--; H--;}
    }
    for (int i: accepted) printf("%d\n",i);
    return 0;
}