#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
    int a,b,c; scanf("%d %d %d",&a,&b,&c);
    vi intermediate {a + b, a - b, a * b};
    if (a % b == 0) intermediate.push_back(a / b);
    int smallest = 1000000000;
    for (int d: intermediate) {
        vi temp {d + c, d - c, d * c};
        if (d % c == 0) temp.push_back(d / c);
        for (int num: temp) {
            if (num >= 0 && num < smallest) smallest = num;
        }
    }
    printf("%d\n",smallest);
    return 0;
}