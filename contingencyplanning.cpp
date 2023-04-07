#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

vi fact {1};
int LIMIT = 1000000000;

int NCR(int n, int r) {
    if (r == 0) return 1;
    if (r > n / 2) return NCR(n, n - r); 
    long res = 1; 
    for (int k = 1; k <= r; ++k){
        res *= n - k + 1;
        res /= k;
    }
    return res;
}

string solve(int n) {
    if (n > fact.size()) return "JUST RUN!!";
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += NCR(n,i) * fact[i];
        if (total > LIMIT) return "JUST RUN!!";
    }
    return to_string(total);
}

int main() {
    int c = 1;
    // precompute factorials <= 10^9
    while (fact.back() * c <= LIMIT) fact.push_back(fact.back() * c++);
    int n; scanf("%d",&n);
    printf(solve(n).c_str());
    return 0;
}