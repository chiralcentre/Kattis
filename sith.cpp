#include <bits/stdc++.h>

using namespace std;

char line[100]; 
int a,b,c;

int main() {
    scanf("%[^\n]",line);
    scanf("%d\n%d\n%d",&a,&b,&c);
    int r = a - b;
    if (r < 0) {
        (r == c) ? printf("JEDI\n") : printf("SITH\n");
    } else printf("VEIT EKKI\n");
    return 0;
}