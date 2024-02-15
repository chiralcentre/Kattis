#include <bits/stdc++.h>

using namespace std;

int N; vector<int> triples;

int main() {
    scanf("%d",&N);
    for (int i = 1; i < 1000; i++) triples.push_back(i * (i + 1) * (i + 2));
    int index = lower_bound(triples.begin(), triples.end(), N) - triples.begin();
    printf("%d\n",index);
    return 0;
}