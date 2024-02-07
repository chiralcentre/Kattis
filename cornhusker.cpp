#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int A,L,N,KWF,T = 0;

int main() {
    for (int i = 0; i < 5; i++) {
        scanf("%d %d",&A,&L);
        T += A * L;
    }
    T /= 5;
    scanf("%d %d",&N,&KWF);
    printf("%d\n", T * N / KWF);
    return 0;
}