#include <bits/stdc++.h>

using namespace std;

int main() {
    int A,B,C; scanf("%d %d %d",&A,&B,&C);
    int I,J,K; scanf("%d %d %d",&I,&J,&K);
    double lowest = min(min((double) A / (double) I, (double) B / (double) J), (double) C / (double) K);
    printf("%f %f %f\n", A - lowest * I, B - lowest * J, C - lowest * K);
    return 0;
}