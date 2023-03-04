#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef unordered_map<int,int> umii;

int A[300000];

//scan from left to right through both arrays at once
//freq[x] is the difference between the number of copies of items x scanned from first array and the numver of copies of items x scanned from second array
//maintain a value v which indicates how many x are there such that freq[x] != 0
//if v = 0, place a divider
//O(N) time
int main() {
    umii freq;
    int N; scanf("%d",&N);
    for (int i = 0; i < N; i++) scanf("%d",&A[i]);
    int v = 0;
    for (int i = 0; i < N; i++) {
        int b; scanf("%d",&b);
        if (freq[A[i]] == 0) v++; //started with zero value, become non zero value
        (freq.find(A[i]) == freq.end()) ? freq[A[i]] = 1 : freq[A[i]]++;
        if (freq[A[i]] == 0) v--; //became zero value
        if (freq[b] == 0) v++; //started with zero value, become non zero value
        (freq.find(b) == freq.end()) ? freq[b] = -1 : freq[b]--;
        if (freq[b] == 0) v--; //became zero value
        printf("%d",b);
        if (i < N - 1) {
            printf(" ");
            if (v == 0) printf("# ");
        }
    }
    printf("\n");
    return 0;
}