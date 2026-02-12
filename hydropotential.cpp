#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll av,ah,bv,bh,cv,ch;

int main() {
    scanf("%lld\n%lld\n%lld\n%lld\n%lld\n%lld\n",&av,&ah,&bv,&bh,&cv,&ch);
    printf("%lld\n", av * ah * 10);
    printf("%lld\n", bv * bh * 10);
    printf("%lld\n", cv * ch * 10);
    return 0;
}