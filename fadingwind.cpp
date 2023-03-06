#include <bits/stdc++.h>

using namespace std;

int main() {
    int h,k,v,s; scanf("%d %d %d %d",&h,&k,&v,&s);
    int d = 0;
    while (h > 0) {
        v += s;
        v -= max(1, v/10);
        if (v >= k) h++;
        else if (0 < v && v < k) {
            if (--h == 0) v = 0;
        } else h = v = 0;
        d += v;
        if (s > 0) s--;
    }
    printf("%d\n",d);
    return 0;
}