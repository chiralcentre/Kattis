#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> I(10,0);
    for (int i = 0; i < 10; i++) scanf("%d",&I[i]);
    printf("%d\n", min({I[5] / I[0], I[6] / I[1], I[7] / I[2], I[8] / I[3], I[9] / I[4]}));
    return 0;
}