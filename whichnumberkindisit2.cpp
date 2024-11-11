#include <bits/stdc++.h>

using namespace std;

int T,N;

unordered_set<int> squares;

int main() {
    scanf("%d",&T);
    for (int i = 0; i * i <= 1000000; i++) squares.insert(i * i);
    for (int i = 0; i < T; i++) {
        scanf("%d",&N);
        bool odd = N % 2, square = squares.find(N) != squares.end();
        if (odd && square) printf("OS\n");
        else if (odd && !square) printf("O\n");
        else if (!odd && square) printf("S\n");
        else printf("EMPTY\n");
    }
    return 0;
}