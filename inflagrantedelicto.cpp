#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef vector<int> vi;
typedef unordered_map<int,int> mii;

int A[200000];
int B[200000];
int C[200000];

const int INF = 1e9;

int LIS(int N) {
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

//k_p is always 2, k_r = length of LCS + 1
int main() {
    int N; scanf("%d", &N);
    mii A_mappings;
    for (int i = 0; i < N; i++) {
        scanf("%d",&A[i]);
        A_mappings[A[i]] = i;
    }
    //time complexity = O(N log N)
    //let C[i] = index of B[i] in A
    //in other words, A[C[i]] = B[i]
    //LCS of A and B is the longest increasing subsequence of C
    mii B_mappings;
    for (int j = 0; j < N; j++) {
        scanf("%d",&B[j]);
        B_mappings[B[j]] = j;
    }
    for (int j = 1; j <= N; j++) C[B_mappings[j]] = A_mappings[j];
    printf("2 %d\n",LIS(N) + 1);
    return 0;
}