#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;

vi SlidingMinWindow(vi &arr, int n, int m) {
    vi windowMins; deque<ii> window;
    for (int i = 0; i < n; i++) {
        while (!window.empty() && window.back().first >= arr[i]) {
            window.pop_back(); // keep window sorted in ascending order
        }
        window.push_back({arr[i],i});
        // check if front element is part of current window
        while (window.front().second <= i - m) window.pop_front();
        if (i + 1 >= m) windowMins.push_back(window.front().first);
    }
    return windowMins;
}

vi SlidingMaxWindow(vi &arr, int n, int m) {
    vi windowMax; deque<ii> window;
    for (int i = 0; i < n; i++) {
        while (!window.empty() && window.back().first < arr[i]) {
            window.pop_back(); // keep window sorted in descending order
        }
        window.push_back({arr[i],i});
        // check if front element is part of current window
        while (window.front().second <= i - m) window.pop_front();
        if (i + 1 >= m) windowMax.push_back(window.front().first);
    }
    return windowMax;
}

int main() {
    int n,m,c; scanf("%d %d %d",&n,&m,&c);
    vi arr(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&arr[i]);
    vi minimum = SlidingMinWindow(arr,n,m);
    vi maximum = SlidingMaxWindow(arr,n,m);
    bool found = false;
    for (int i = 0; i < minimum.size(); i++) {
        if (maximum[i] - minimum[i] <= c) {
            found = true;
            printf("%d\n",i + 1);
        }
    }
    if (!found) printf("NONE\n");
    return 0;
}