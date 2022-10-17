#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> x_coords;
    vector<int> y_coords;
    for (int i = 0; i < N; i++) {
        int x,y; cin >> x >> y;
        x_coords.push_back(x); y_coords.push_back(y);
    }
    sort(x_coords.begin(),x_coords.end());
    sort(y_coords.begin(),y_coords.end());
    long long sum = 0;
    for (int i = 0; i < N; i++){
        sum += abs(i + 1 - x_coords[i]) + abs(i + 1  - y_coords[i]);
    }
    cout << sum;
    return 0;
}