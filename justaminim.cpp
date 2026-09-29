#include <bits/stdc++.h>

using namespace std;

int N,c;

unordered_map<int, double> notes = {
    {0, 2},
    {1, 1},
    {2, 0.5},
    {4, 0.25},
    {8, 0.125},
    {16, 0.0625}
};

int main() {
    scanf("%d",&N);
    double length = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d",&c);
        length += notes[c];
    }
    printf("%lf\n",length);
    return 0;
}