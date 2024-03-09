#include <bits/stdc++.h>

using namespace std;

unordered_map<int,int> cv = {{1, 1}, {12, 2}, {123, 3}, {1234, 4}, 
                            {12345, 5}, {123456, 6}, {1234567, 7},
                            {12345678, 8}, {123456789, 9}};
int n;

int main() {
    scanf("%d",&n);
    (cv.find(n) == cv.end()) ? printf("-1\n") : printf("%d\n",cv[n]);
    return 0;
}