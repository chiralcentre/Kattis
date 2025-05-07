#include <bits/stdc++.h>

using namespace std;

int N,M,t,s1 = 0,s2 = 0;

int main() {
    scanf("%d %d",&N,&M);
    for (int i = 0; i < N; i++) {
        scanf("%d",&t);
        s1 += t;
    }
    for (int i = 0; i < M; i++) {
        scanf("%d",&t);
        s2 += t;
    }
    if (s1 > s2) printf("Button 1\n");
    else if (s1 == s2) printf("Oh no\n");
    else printf("Button 2\n");
    return 0;
}