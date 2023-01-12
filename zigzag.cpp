#include <bits/stdc++.h>

using namespace std;

int main() {
    int k; scanf("%d",&k);
    //find minimum number of differences required
    //25 is the maximum consecutive difference ('a' and 'z')
    int d = k % 25  ? k / 25 + 1 : k / 25;
    if (d == 1) {
        printf("a");
        printf("%c",char(97 + k));
    } else if (d == 2) {
        int m = k % 2 ? k / 2 + 1 : k / 2;
        printf("a");
        printf("%c",char(97 + m));
        printf("%c", k % 2 ? 'b' : 'a');
    } else {
        // assume last d - 2 differences are 25
        int R = (d - 2) * 25; int L = k - R;
        if (L % 2) {L++; R--;}
        printf("a");
        printf("%c",char(97 + L / 2));
        printf("a");
        char prev = 'a';
        while (R >= 25) {
            prev = prev == 'a' ? 'z' : 'a';
            R -= 25; printf("%c",prev);
        }
        if (R > 0) printf("%c",prev == 'z' ? char('z' - R) : char('a' + R));
    }
    return 0;
}