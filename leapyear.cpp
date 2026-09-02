#include <bits/stdc++.h>

using namespace std;

int y;

string solve(int y) {
    if (y % 4 == 0) {
        if (y % 100 == 0) {
            return (y % 400 == 0) ? "True" : "False";
        } else return "True";
    } else return "False";
}

int main() {
    scanf("%d",&y);
    printf("%s\n",solve(y).c_str());
    return 0;
}