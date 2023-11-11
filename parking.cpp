#include <bits/stdc++.h>

using namespace std;

int A,B,C,X,Y,parked[101];
int main() {
    memset(parked,0,sizeof(parked));
    scanf("%d %d %d",&A,&B,&C);
    for (int i = 0; i < 3; i++) {
        scanf("%d %d",&X,&Y);
        for (int j = X; j < Y; j++) parked[j]++;
    }
    int total = 0;
    for (int p: parked) {
        if (p == 1) total += A;
        else if (p == 2) total += B << 1;
        else if (p == 3) total += C * 3;
    }
    printf("%d\n",total);
    return 0;
}