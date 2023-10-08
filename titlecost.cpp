#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

string title; double cost;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> title >> cost;
    cout << setprecision(10) << min(cost,double(title.length())) << "\n";
}