#include <bits/stdc++.h>

using namespace std;

int main() {
    int R,C; scanf("%d %d",&R,&C);
    //number of breaks required to split chocolate bar into 1 x 1 pieces is R * C - 1
    int breaks = R * C - 1;
    printf(breaks % 2 ? "Alf\n" : "Beata\n");
    return 0;
}