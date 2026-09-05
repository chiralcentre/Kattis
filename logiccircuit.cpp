#include <bits/stdc++.h>

using namespace std;

int main() {
    bool A,B,C;
    cin >> A >> B >> C;
    cout << (int)((!B && A) || (!A && C));
}