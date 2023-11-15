#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int T,N,total,arr[20];

unordered_map<int,vi> sums;

int get_bit(int num, int bit) {
    int temp = (1 << bit) & num;
    return (temp == 0) ? 0 : 1;
}

void print_vector(vi &vec) {
    int L = vec.size();
    for (int j = 0; j < L; j++) {
        printf("%d", vec[j]);
        if (j < L - 1) printf(" ");
    }
    printf("\n");
}

void solve(int v, int c) {
    printf("Case #%d:\n",c);
    // start from 1 to ignore empty subset
    for (int i = 1; i < (1 << v); i++) {
        vi st; int total = 0;
        for (int j = 0; j < v; j++) {
            if (get_bit(i, j) == 1) {
                st.push_back(arr[j]);
                total += arr[j];
            }
        }
        if (sums.find(total) != sums.end()) {
            print_vector(sums[total]);
            print_vector(st);
            return;
        } else sums[total] = st;
    }
    printf("Impossible\n");
}

int main() {
    scanf("%d",&T);
    for (int i = 1; i <= T; i++) {
        scanf("%d",&N);
        for (int j = 0; j < N; j++) scanf("%d",&arr[j]);
        sums.clear();
        solve(N,i);
    }
    return 0;
}