#include <bits/stdc++.h>

using namespace std;

int d;

void print_edge(int d) {
    for (int i = 0; i < d; i++) {
        printf("*");
        if (i < d - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    scanf("%d",&d);
    print_edge(d);
    for (int i = 0; i < d - 2; i++) {
        printf("*");
        for (int j = 0; j < 2 * d - 3; j++) printf(" ");
        printf("*\n");
    }
    if (d > 1) print_edge(d);
    return 0;
}