#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll arr[1000000];
int n;

int binary_search(ll num) {
    int low = 0, mid = 0, high = n - 1;
    while (low <= high) {
        mid = low + ((high - low) >> 1);
        if (arr[mid] < num) low = mid + 1;
        else if (arr[mid] > num) high = mid - 1;
        else return 1;
    }
    return 0;
}

//perform n binary searches in O(log n) time each
//note that all values generated are guaranteed to be unique
int main() {
    ll m,a,c,x0; 
    scanf("%d %lld %lld %lld %lld",&n,&m,&a,&c,&x0);
    ll prev = x0;
    for (int i = 0; i < n; i++) {
        arr[i] = (a * prev + c) % m;
        prev = arr[i];
    }
    int ans = 0;
    for (int i = 0; i < n; i++) ans += binary_search(arr[i]);
    printf("%d\n",ans);
    return 0;
}