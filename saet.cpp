#include <bits/stdc++.h>

using namespace std;

int a,b;

string solve(int a, int b) {
    if (a < 21 && b < 21) return "?";
    else if (a >= 21 && b < 21) {
        // A wins if a = 21 and b <= 19 or a = 22 and b = 20
        if ((a == 21 && b <= 19) || (a == 22 && b == 20)) return "A";
        if (a == 21 && b == 20) return "?";
        return "!";
    } else if (b >= 21 && a < 21) {
        // B wins if b = 21 and a <= 19 or b = 22 and a = 20
        if ((b == 21 && a <= 19) || (b == 22 && a == 20)) return "B";
        if (b == 21 && a == 20) return "?";
        return "!";
    } else { // a >= 21 and b >= 21
        if (a == 30 && b == 29) return "A";
        if (a == 29 && b == 30) return "B";
        if (a == 30 && b == 30) return "!";
        if (a - b == 2) return "A";
        if (b - a == 2) return "B";
        if (abs(a - b) < 2) return "?";
        return "!";
    }
}

int main() {
    scanf("%d-%d",&a,&b);
    printf("%s\n",solve(a,b).c_str());
    return 0;
}