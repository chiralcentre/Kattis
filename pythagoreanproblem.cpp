#include <bits/stdc++.h>

using namespace std;

int a,b;

bool isSquare(int num) {
    int a = floor(double(sqrt(num)));
    int b = ceil(double(sqrt(num)));
    return a * a == num || b * b == num;
}

int main() {
    scanf("%d %d",&a,&b);
    if (a == b) {
        printf("Pythagoras is sad :(\n");
    } else {
        if (a > b) swap(a, b); // ensure a < b
        // two possibilities: a ^ 2 + b ^ 2 = c ^ 2, a ^ 2 + c ^ 2 = b ^ 2
        int c = a * a + b * b;
        int d = b * b - a * a;
        if (isSquare(c)) printf("%d\n", int(sqrt(c)));
        else if (isSquare(d)) printf("%d\n", int(sqrt(d)));
        else printf("Pythagoras is sad :(\n");
    }
    return 0;
}