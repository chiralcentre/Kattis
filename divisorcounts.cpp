#include <bits/stdc++.h>

using namespace std;

int lst[3000001];

//O(N lg N) approach
//for every number i from 2 to N, find all numbers divisible by i.
int main() {
    int N; scanf("%d",&N);
    for (int i = 0; i <= N; i++) lst[i] = 1;
    for (int i = 2; i <= N; i++) {
        for (int j = i; j <= N; j += i) lst[j]++;
    }
    for (int i = 1; i <= N; i++) printf("%d\n",lst[i]);
    return 0;
}