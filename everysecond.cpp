#include <bits/stdc++.h>

using namespace std;

int sh,sm,ss,eh,em,es;

int DAY = 24 * 60 * 60;
int HOUR = 60 * 60;
int MIN = 60;

int main() {
    scanf("%d : %d : %d", &sh, &sm, &ss);
    scanf("%d : %d : %d", &eh, &em, &es);
    int start = sh * HOUR + sm * MIN + ss;
    int end = eh * HOUR + em * MIN + es;
    int r = end - start;
    if (r < 0) r += DAY;
    printf("%d\n", r);
    return 0;
}