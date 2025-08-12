#include <bits/stdc++.h>

using namespace std;

int N,K;

int main() {
    scanf("%d %d",&N,&K);
    printf("%d\n",N / K + (N % K > 0));
    return 0;
}