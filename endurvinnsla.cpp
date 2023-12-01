#include <bits/stdc++.h>

using namespace std;

char line[100]; string s; int a,b,p,n,t = 0;

int main() {
    // actual name of city does not matter
    // mix of cin and printf is used because first line can be empty
    getline(cin,s);
    scanf("%d.%d",&a,&b);
    p = a * 100 + b;
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%s",line);
        if (strcmp(line,"ekki") == 0) {
            scanf("%s", line);
            t++;
        }
    }
    (t * 100 <= p * n) ? printf("Jebb\n") : printf("Neibb\n");
    return 0;
}