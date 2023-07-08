#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef vector<int> vi;
typedef unordered_map<int,int> mii;

int A[62501], B[62501],t,n,p,q;
vi ts, C;

int LIS(int N) {
    if (N == 0) return 0;
    vi L; L.push_back(C[0]);
    for (int i = 1; i < N; i++) {
        //add to LIS
        if (C[i] > L.back()) L.push_back(C[i]);
        //replace with better candidate
        else {
            int pos = lower_bound(L.begin(), L.end(), C[i]) - L.begin();
            L[pos] = C[i];
        }
    }
    return L.size();
}

int main() {
    scanf("%d",&t);
    for (int k = 1; k <= t; k++) {
        C.clear(); // reinstantiate C as empty vector
        scanf("%d %d %d", &n, &p, &q);
        for (int i = 0; i < p + 1; i++) scanf("%d", &A[i]); 
        for (int i = 0; i < q + 1; i++) scanf("%d", &B[i]);
        // find LCS of the two sequences
        mii A_mappings, B_mappings;
        for (int i = 0; i < p + 1; i++) A_mappings[A[i]] = i;
        //time complexity = O(N log N)
        //record position of each element in A in B into C in descending order
        //LCS of A and B is the longest increasing subsequence of C
        for (int i = 0; i < q + 1; i++) B_mappings[B[i]] = i; // no repeats
        for (int i = 0; i < p + 1; i++) {
            if (B_mappings.find(A[i]) != B_mappings.end()) C.push_back(B_mappings[A[i]]);
        }
        printf("Case %d: %d\n", k, LIS(int(C.size())));
    }
    return 0;
}