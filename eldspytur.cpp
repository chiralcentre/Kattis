#include <bits/stdc++.h>

using namespace std;

int n,k;

int main() {
    scanf("%d %d",&n,&k);
    if (k >= n) printf("Jebb\n");
    else {
        // need opponent to have a multiple of k + 1 to choose from
        // at any point of time,no matter what the opponent chooses, Benni can choose a number to make the opponent go to a multiple of k + 1
        // when there is k + 1 matches left, no matter what opponent chooses, Benni can take all that is left over and win
        int rem = n % (k + 1);
        printf(rem == 0 ? "Neibb\n" : "Jebb\n");
    }
    return 0;
}