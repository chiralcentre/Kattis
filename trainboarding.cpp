#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int N,L,P; scanf("%d %d %d",&N,&L,&P);
    vi doors(N,0), boarded(N,0);
    int longest = -1;
    doors[0] = L / 2;
    for (int i = 1; i < N; i++) doors[i] += doors[i - 1] + L;
    for (int i = 0; i < P; i++) {
        int x; scanf("%d",&x);
        if (x <= doors[0]) {
            boarded[0]++; longest = max(doors[0] - x, longest);
        } else if (x >= doors.back()) {
            boarded[N - 1]++; longest = max(x - doors.back(), longest);
        } else {
            vi::iterator lower, upper;
            lower = lower_bound(doors.begin(), doors.end(), x);
            upper = upper_bound(doors.begin(), doors.end(), x);
            int L = lower - doors.begin(), U = upper - doors.begin();
            if (doors[L] > x) L --;
            //printf("doors[%d] = %d, doors[%d] = %d\n",L,doors[L],U,doors[U]);
            if (x - doors[L] < doors[U] - x) {
                boarded[L]++; longest = max(x - doors[L], longest);
            } else {
                boarded[U]++; longest = max(doors[U] - x, longest);
            }
        }
    }
    printf("%d\n",longest);
    printf("%d\n",*max_element(boarded.begin(),boarded.end()));
    return 0;
}