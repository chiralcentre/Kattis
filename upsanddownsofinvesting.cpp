#include <bits/stdc++.h>

using namespace std;

int main() {
    int s,n,m,curr,prev; scanf("%d %d %d",&s,&n,&m);
    //dir = 1 for increasing, dir = 0 for decreasing
    int riseLen = 1, fallLen = 1, peaks = 0, valleys = 0, dir = -1;
    scanf("%d",&prev);
    for (int i = 1; i < s; i++) {
        scanf("%d",&curr);
        if (curr > prev) {
            if (dir == 1) riseLen++;
            else {
                if (riseLen >= n && fallLen >= n) peaks++;
                dir = 1; riseLen = 2;
            }
        } else {
            if (dir == 0) fallLen++;
            else {
                if (fallLen >= m && riseLen >= m) valleys++;
                dir = 0; fallLen = 2;
            }
        }
        prev = curr;
    }
    if (dir == 1 && fallLen >= m && riseLen >= m) valleys++;
    else if (dir == 0 && riseLen >= n && fallLen >= n) peaks++;
    printf("%d %d\n",peaks,valleys);
    return 0;
}