#include <bits/stdc++.h>

using namespace std;

//digits[i] = number of digits in factorial(i)
int digits[1000001], N;

int main() {
    digits[0] = 1;
    double c = 0;
    // number of digits in number n = floor(log10(n)) + 1
    for (int i = 1; i < 1000001; i++) {
        c += log10(i);
        digits[i] = floor(c) + 1;
    }
    while (scanf("%d",&N) == 1) printf("%d\n",digits[N]);
    return 0;
}