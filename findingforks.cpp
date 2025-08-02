#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int n;

int main() {
    scanf("%d",&n);
    vi forks(n, 0);
    for (int i = 0; i < n; i++) scanf("%d",&forks[i]);
    sort(forks.begin(), forks.end());
    printf("%d\n",forks[0] + forks[1]);
    return 0;
}