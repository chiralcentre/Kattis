#include <bits/stdc++.h>
#include <string>

using namespace std;

bool inRange(int a, int b, int k) {
    int c = min(a,b), d = max(a,b);
    return c <= k && k <= d;
}

string solve(int m,int l,int M,int L,int tM,int tL) {
    int t = 0;
    if (tM < tL) {// Monica has to be served first
        t += abs(m) + abs(m - M);
        if (t > tM) return "impossible";
        if (inRange(0,M,l) && abs(m) < abs(M)) {
            l = m;
        } 
        t += abs(l - M) + abs(L - l);
        return t > tL ? "impossible" : "possible";
    } else {//Lydia is served first
        t += abs(l) + abs(l - L);
        if (t > tL) return "impossible";
        if (inRange(0,L,m) && abs(l) < abs(L)) {
            m = l;
        }
        t += abs(m - L) + abs(M - m);
        return t > tM ? "impossible" : "possible";
    }
}

int main() {
    int m,l; scanf("%d %d",&m,&l);
    int M,L; scanf("%d %d",&M,&L);
    int tM,tL; scanf("%d %d",&tM,&tL);
    printf("%s\n",solve(m,l,M,L,tM,tL).c_str());
    return 0;
}