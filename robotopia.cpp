#include <bits/stdc++.h>

using namespace std;

string solve(int l1,int a1,int l2,int a2,int lt,int at) {
    int m1 = min(lt/l1,at/a1);
    int m2 = min(lt/l2,at/a2);
    if (m1 == 0 || m2 == 0) return "?";
    int s1 = -1, s2 = -1;
    for (int i = 1; i <= m1; i++) {
        int r1 = lt - i * l1, r2 = at - i * a1;
        if (r1 % l2 == 0 &&  r2 % a2 == 0 && r1 / l2 == r2 / a2 and r1 / l2 > 0) {
            if (s1 == -1 and s2 == -1) {s1 = i; s2 = r1 / l2;}
            else return "?";
        }
    }
    if (s1 > -1 and s2 > -1) return to_string(s1) + " " + to_string(s2);
    return "?";
}

int main() {
    int N; scanf("%d",&N);
    while (N--) {
        int l1,a1,l2,a2,lt,at; 
        scanf("%d %d %d %d %d %d",&l1,&a1,&l2,&a2,&lt,&at);
        printf("%s\n",solve(l1,a1,l2,a2,lt,at).c_str());
    }
    return 0;
}