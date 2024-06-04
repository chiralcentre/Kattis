#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> // Common file 
#include <ext/pb_ds/tree_policy.hpp> 
#include <functional> // for less 

using namespace __gnu_pbds;
using namespace std;

typedef tree<pair<double, int>, null_type,
    less<pair<double, int>>, rb_tree_tag,
    tree_order_statistics_node_update> ordered_set;

int N, a, counter = 0;
double total = 0;

int main() {
    scanf("%d",&N);
    ordered_set P;
    for (int i = 1; i <= N; i++) {
        scanf("%d", &a);
        P.insert({a, i});
        total += a;
        pair<double,int> temp = make_pair(total / i, 0);
        P.insert(temp);
        int rank = P.order_of_key(temp);
        if (rank * 2 > i) counter++;
        P.erase(temp);
    }
    printf("%d\n", counter);
    return 0;
}