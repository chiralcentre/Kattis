#include <bits/stdc++.h>

using namespace std;

int G,N,a,b,c = 2;

int main() {
    unordered_map<int, pair<int, int>> myMap;
    myMap[1] = make_pair(2, 3);
    myMap[2] = make_pair(1, 3);
    myMap[3] = make_pair(1, 2);
    scanf("%d\n%d",&G,&N);
    for (int i = 0; i < N; i++) {
        scanf("%d %d",&a,&b);
        if (a == c) swap(b, c);
        else if (b == c) swap(a, c);
    }
    if (c == G) printf("%d %d",myMap[c].first,myMap[c].second);
    else printf("%d %d\n",G,c);
    return 0;
}